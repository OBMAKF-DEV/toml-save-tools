from typing import TextIO, Any, Type

Game: object = Type['Game']


def save_game(func):
    """A decorated context manager for saving data.
    
    Saves all player and game data to a save file.
    
    Notes:
        - This decorator is to be used in the main game class above methods that requires the game to be saved.
    
    Args:
        func (function | Any): The function to decorate over.
    
    Example:
        ``>>> class Game(object):``
        
        ``>>>     @save_game``
        
        ``>>>     def event(self, ...):``
        
        ``>>>         ...``
    
    Returns:
        The wrapped function logic.
    """
    
    def wrapper(cls: Game, *args, **kwargs):
        with open(f"{cls.save_file}.toml", 'w') as file:
            # Save player attribute values into the savefile.
            file.write('[player_data]\n')
            for k, v in cls.player.__dict__.items:
                file.write(f"{k} = {v}\n")
            file.write('\n')
            # Save game specific attribute values into the savefile.
            file.write('[game_data]\n')
            # todo ... ( add game attributes here )
        return func(*args, **kwargs)
    return wrapper
