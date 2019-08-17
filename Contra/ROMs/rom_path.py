"""A method to load a ROM path."""
import os


def rom_path():
    """
    Return the ROM filename for a game and ROM mode.


    Returns (str):
        the ROM path

    """

    rom = "contra.nes"
    rom = os.path.join(os.path.dirname(os.path.abspath(__file__)), rom)

    return rom


# explicitly define the outward facing API of this module
__all__ = [rom_path.__name__]
