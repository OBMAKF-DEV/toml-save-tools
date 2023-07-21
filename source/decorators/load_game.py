from typing import BinaryIO, Any, Type
import tomli

Game: object = Type['Game']


def load_game(func):
    """A decorated context manager for loading data.

    Loads all player and game data to a save file.

    Notes:
        - This decorator is to be used in the main game class above methods that requires loading game data.

    Args:
        func (function | Any): The function to decorate over.

    Example:
        ``>>> class Game(object):``

        ``>>>     @load_game``

        ``>>>     def start(self, ...):``

        ``>>>         ...``

    Returns:
        The wrapped function logic.
    """
    
    def wrapper(cls: Game, *args, **kwargs):
        with open(f"{cls.save_file}.toml", 'rb') as file:
            _data = tomli.load(file)
            
            # load player attributes from the savefile.
            for k, v in _data['player_data'].items():
                cls.player[k] = v
            
            # load game specific attributes from the savefile.
            for k, v in _data['game_data'].items():
                cls[k] = v
        return func(*args, **kwargs)
    return wrapper
