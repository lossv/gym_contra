import os

from gym import spaces
from .nesenv import NESEnv

package_directory = os.path.dirname(os.path.abspath(__file__))


class Contra_env(NESEnv):
    def __init__(self):
        super().__init__()
        print("1346")
        print("package_directory ", package_directory)
        self.lua_interface_path = os.path.join(package_directory, '../lua/score.lua')
        self.rom_file_path = os.path.join(package_directory, '../ROMs/contra.nes')
        self.actions = [
            'R', 'UR', 'DR',
            'B', 'URB', 'DRB', 'RB',
            'AB', 'RAB', 'URAB', 'DRAB'
        ]
        self.action_space = spaces.Discrete(len(self.actions))
        print("self.action_space ")
        print(self.action_space)
