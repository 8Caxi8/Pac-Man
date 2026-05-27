from abc import ABC, abstractmethod
from .map import Map


class GhostStrategy(ABC):
    @abstractmethod
    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int]) -> tuple[int, int]:
        pass


class AgressorStrategy(GhostStrategy):
    def move(self, pos, player_pos): ...


class AmbusherStrategy(GhostStrategy):
    def move(self, pos, player_pos): ...


class UnpredictableStrategy(GhostStrategy):
    def move(self, pos, player_pos): ...


class WandererStrategy(GhostStrategy):
    def move(self, pos, player_pos): ...
