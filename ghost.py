from enum import Enum

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
                
            case Strategy.AMBUSHER:
            
            case Strategy.UNPREDICTABLE:

            case Strategy.WANDERER:
            
