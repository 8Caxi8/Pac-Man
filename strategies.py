from abc import ABC, abstractmethod
from .map import Map


class GhostStrategy(ABC):
    def __init__(self, map: Map, home: tuple[int, int]) -> None:
        self._map = map
        self._home = home

    @abstractmethod
    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int]) -> tuple[int, int]:
        pass


class AgressorStrategy(GhostStrategy):
    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int]) -> tuple[int, int]:
        return self._map.next_step_toward(pos, player_pos) or pos


class AmbusherStrategy(GhostStrategy):
    def move(self, pos, player_pos): ...


class UnpredictableStrategy(GhostStrategy):
    def move(self, pos, player_pos): ...


class WandererStrategy(GhostStrategy):
    def move(self, pos, player_pos): ...
