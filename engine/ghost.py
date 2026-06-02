import random
from enum import Enum
from .strategies import (GhostStrategy, AgressorStrategy, AmbusherStrategy,
                         WandererStrategy, UnpredictableStrategy)
from .map import Map


class GhostError(Exception):
    pass


class Strategy(Enum):
    AGRESSOR = "Agressor"
    AMBUSHER = "Ambusher"
    UNPREDICTABLE = "Unpredictable"
    WANDERER = "Wanderer"


class State(Enum):
    CHASE = "Chase"
    SCATTER = "Scatter"
    FRIGHTENED = "Frightened"
    EATEN = "Eaten"


class Ghost():
    def __init__(self, strategy: Strategy,
                 home: tuple[int, int],
                 map: Map) -> None:
        self._strategy = strategy
        self._home = home
        self._map = map
        self._state = State.CHASE
        self._position = self._home
        self._set_strategy(strategy)

    def _set_strategy(self, strategy: Strategy) -> None:
        self._behaviour: GhostStrategy

        match strategy:
            case Strategy.AGRESSOR:
                self._behaviour = AgressorStrategy(self._map, self._home)
            case Strategy.AMBUSHER:
                self._behaviour = AmbusherStrategy(self._map, self._home)
            case Strategy.UNPREDICTABLE:
                self._behaviour = UnpredictableStrategy(self._map, self._home)
            case Strategy.WANDERER:
                self._behaviour = WandererStrategy(self._map, self._home)
            case _:
                raise GhostError(f"Unknown strategy: {strategy}")

    def move(self, game_state: dict[str, tuple[int, int]]) -> None:
        match self._state:
            case State.EATEN:
                if self._position == self._home:
                    self.change_state(State.CHASE)
                    return self.move(game_state)

                game_state["player_pos"] = self._home
                self._position = self._behaviour.move(**game_state)

            case State.SCATTER:
                neighbors = self._map.neighbors(self._position)
                if not neighbors:
                    raise GhostError("Error selecting Neighbors from "
                                     f"{self._position}")

                self._position = random.choice(neighbors)

            case State.FRIGHTENED:
                neighbors = self._map.neighbors(self._position)
                player_pos = game_state["player_pos"]
                if not neighbors:
                    raise GhostError("Error selecting Neighbors from "
                                     f"{self._position}")

                self._position = max(
                    neighbors,
                    key=lambda n: abs(n[0] - player_pos[0]) +
                    abs(n[1] - player_pos[1])
                )

            case State.CHASE:
                self._position = self._behaviour.move(**game_state)

    def change_state(self, state: State) -> None:
        if state not in State:
            raise GhostError(f"Unknown state: {state}")

        self._state = state

    def get_state(self) -> State:
        return self._state

    def get_position(self) -> tuple[int, int]:
        return self._position
