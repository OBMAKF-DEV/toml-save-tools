from typing import Type
import tomli

Game: object = Type['Game']


def load(cls: Game, subject: str, _kw: str | list[str]) -> str | int | list | None:
    with open(f"{cls.save_file}.toml", 'rb') as file:
        _data = tomli.load(file)
    _data = _data[subject]
    try:
        if isinstance(_kw, list):
            return [_data[k] for k in _kw]
        return _data[_kw]
    except KeyError as exc:
        raise KeyError(exc) from exc
