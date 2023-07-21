# /=============================================\
# |  File-Path  | ../savefile/__init__.py       |
# |~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |    Package  | savefile                      |
# |~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |             | - decorators.load_game        |
# |    Modules  | - decorators.save_game        |
# |             | - utils.load                  |
# |~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |     Github  | https://github.com/OBMAKF-DEV |
# \=============================================/

"""This Package provides save file functionality for saving and loading from a TOML save file."""

# Package-level imports
from .source.decorators import save_game, load_game
from .source.utils import load

__all__ = ['save_game', 'load_game', 'load']
