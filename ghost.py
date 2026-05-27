from enum import Enum
from .strategies import AgressorStrategy, AmbusherStrategy, WandererStrategy, UnpredictableStrategy


class GhostError(Exception):
    pass


class Strategy(Enum):
    AGRESSOR = "Agressor"
    AMBUSHER = "Ambusher"
    UNPREDICTABLE = "Unpredictable"
    WANDERER = "Wanderer"


class Ghost():
    def __init__(self, strategy: Strategy, home: tuple[int, int]) -> None:
        self._strategy = strategy
        self._home = home
        self._set_strategy(strategy)

    def _set_strategy(self, strategy: Strategy) -> None:
        match strategy:
            case Strategy.AGRESSOR:
                self._behaviour = AgressorStrategy()
            case Strategy.AMBUSHER:
                self._behaviour = AmbusherStrategy()
            case Strategy.UNPREDICTABLE:
                self._behaviour = UnpredictableStrategy()
            case Strategy.WANDERER:
                self._behaviour = WandererStrategy()
