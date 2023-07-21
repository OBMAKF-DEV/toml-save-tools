# toml-save-tools
This package adds simple Python decorator methods and functions for reading and writing TOML save files.

## About
This package is being developed to add save functionality to Python games.
The package requires the you to install ***tomli - v2.0.1*** *(or higher)*

*To install tomli run:*

```bash 
pip install tomli
```

*To ensure that* **pip** *is up to-date run:*

```bash
pip install --upgrade pip
```

## How to use

Using the `load_game` decorator...

```python3
class Game: 
	def __init__(self, ...):
		self.player = ...

  @load_game
	def start(self, ...):
		# implement the game logic here.
```

This assigns any saved values to `Game` and `Game.player`.

---

Using the `save_game` decorator...

```python3
class Game:
	def __init__(self, ...):
		self.player = ...

	@save_game
	def event(self, ...):
		# implement the event logic here.
```

This saves the `Game` and `Game.player` attribute values to the save file.

---

Using the `load` method to retrive a single element...

```python3
game = Game(...)

hp = load(game, subject='player_data', _kw='health')
# 100
```
... And to retrieve multiple elements...

```python3
game = Game(...)

elements = load(game, subject='player_data', _kw=['health', 'stamina', 'xp'])
# [100, 20, 120]
```

---	
