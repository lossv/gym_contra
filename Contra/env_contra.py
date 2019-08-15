"""An OpenAI Gym interface to the NES game <TODO: Contra>"""
import numpy as np
from nes_py import NESEnv
import os
from Contra.ROMs.decode_target import decode_target

_STAGE_OVER_ENEMIES = np.array([0x2D, 0x31])
_ENEMY_TYPE_ADDRESSES = [0x0016, 0x0017, 0x0018, 0x0019, 0x001A]


class ContraEnv(NESEnv):
    """An OpenAI Gym interface to the NES game <TODO: Contra>"""

    reward_range = (-15, 15)

    def __init__(self, lost_levels=False, target=None):
        """
        Initialize a new Super Mario Bros environment.

        Args:
            lost_levels (bool): whether to load the ROM with lost levels.
                - False: load original Super Mario Bros.
                - True: load Super Mario Bros. Lost Levels
            target (tuple): a tuple of the (world, stage) to play as a level

        Returns:
            None

        """
        # The .nes file path name abso
        self._abs_path = os.getcwd()
        self._rom_name = '/ROMs/contra.nes'
        self._rom_path = self._abs_path + self._rom_name
        self._dead_count = 0

        # initialize the super object with the ROM path
        super(ContraEnv, self).__init__(self._rom_path)
        # set the target world, stage, and area variables
        target = decode_target(target, lost_levels)
        self._target_world, self._target_stage, self._target_area = target

        # setup a variable to keep track of the last frames x position
        self._x_position_last = 0
        # reset the emulator
        self.reset()
        # skip the start screen
        self._skip_start_screen()
        # create a backup state to restore from on subsequent calls to reset
        self._backup()
        print("Make_done")

    @property
    def is_single_stage_env(self):
        """Return True if this environment is a stage environment."""
        return self._target_world is not None and self._target_area is not None

    def _read_mem_range(self, address, length):
        """
        Read a range of bytes where each byte is a 10's place figure.

        Args:
            address (int): the address to read from as a 16 bit integer
            length: the number of sequential bytes to read

        Note:
            this method is specific to Mario where three GUI values are stored
            in independent memory slots to save processing time
            - score has 6 10's places
            - coins has 2 10's places
            - time has 3 10's places

        Returns:
            the integer value of this 10's place representation

        """
        return int(''.join(map(str, self.ram[address:address + length])))

    def _skip_start_screen(self):
        """Press and release start to skip the start screen."""
        # press and release the start button
        self._frame_advance(8)
        self._frame_advance(0)
        self._frame_advance(8)
        self._frame_advance(0)

        while True:
            self._frame_advance(8)
            self._frame_advance(0)
            if self.ram[0x002C] == 4:
                break

    @property
    def _get_game_state(self):
        """0038 - Game Status (00 - playing, 01 - game over)"""
        return self.ram[0x0038]

    @property
    def _life(self):
        """Return the number of remaining lives."""
        return self.ram[0x0032]

    @property
    def _x_position(self):
        """Return the current horizontal position."""
        return self.ram[0x0334]

    @property
    def _y_pixel(self):
        """Return the current vertical position."""
        return self.ram[0x031A]

    @property
    def _y_position(self):
        """Return the current vertical position."""
        # check if player's is above the viewport (the score board area)
        return 255 - self._y_pixel

    @property
    def _player_state(self):
        """
        Return the current player state.

        Note:
           Alive Status (00 - Dead, 01 - Alive, 02 - Dying)
        """
        return self.ram[0x0090]

    @property
    def _is_dying(self):
        """Return True if Mario is in dying animation, False otherwise."""
        return self._player_state == 2

    @property
    def _is_dead(self):
        """Return True if Mario is dead, False otherwise."""
        if self._player_state == 0:
            self._dead_count += 1
            # print("Dead count", self._dead_count)
        return self._player_state == 0

    @property
    def _is_game_over(self):
        """Return True if the game has ended, False otherwise."""
        # get the game state Game Status (00 - playing, 01 - game over)
        return self._get_game_state == 1

    # MARK: Reward Function
    @property
    def _x_reward(self):
        """Return the reward based on left right movement between steps."""
        # print("self._x_position", self._x_position)
        _reward = self._x_position - self._x_position_last
        # print("_reward ", _reward)
        self._x_position_last = self._x_position
        # TODO: check whether this is still necessary
        # resolve an issue where after death the x position resets. The x delta
        # is typically has at most magnitude of 3, 5 is a safe bound
        if _reward < -5 or _reward > 5:
            return 0

        return _reward

    @property
    def _death_penalty(self):
        """Return the reward earned by dying."""
        if self._is_dying or self._is_dead:
            return -25

        return 0

    # MARK: nes-py API calls
    def _will_reset(self):
        """Handle and RAM hacking before a reset occurs."""
        self._x_position_last = 0
        self._dead_count = 0

    def _did_reset(self):
        """Handle any RAM hacking after a reset occurs."""
        self._x_position_last = self._x_position
        self._dead_count = 0

    # have to recode
    def _did_step(self, done):
        """
        Handle any RAM hacking after a step occurs.

        Args:
            done: whether the done flag is set to true

        Returns:
            None

        """
        # if done flag is set a reset is incoming anyway, ignore any hacking
        if done:
            return
        # if players is dying, then cut to the chase and kill hi,
        if self._is_dying:
            self._frame_advance(0)
            self._frame_advance(0)
            self._frame_advance(0)
            self._frame_advance(0)
            self._frame_advance(0)
            self._frame_advance(0)
            self._frame_advance(0)
        if self._is_game_over:
            self._frame_advance(32)
            self._frame_advance(8)

    def _get_reward(self):
        """Return the reward after a step occurs."""
        return self._x_reward + self._death_penalty + self._get_boss_defeated_reward()

    @property
    def _get_boss_defeated(self):
        """
        002C - Screen Type
        00 - menu
        04 - normal gameplay
        05 - credits
        06 - continue
        08 - boss defeated
        09 - boss defeat (minor different from prev. one - hard to describe)
        :return:
        """
        return self.ram[0x002C] == 8

    def _get_boss_defeated_reward(self):
        if self._get_boss_defeated:
            return 30
        return 0

    def _get_done(self):
        """Return True if the episode is over, False otherwise."""
        if self._is_game_over or self._get_boss_defeated:
            return True
        return False

    def _get_info(self):
        """Return the info after a step occurs"""
        return dict(
            life=self._life,
            dead=self._is_dead,
            done=self._get_done,
            status=self._player_state,
            x_pos=self._x_position,
            y_pos=self._y_position,
        )


# explicitly define the outward facing API of this module
__all__ = [ContraEnv.__name__]
