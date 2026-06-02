from abc import ABC, abstractmethod
from .map import Map


class GhostStrategy(ABC):
    def __init__(self, map: Map, home: tuple[int, int]) -> None:
        self._map = map
        self._home = home

    @abstractmethod
    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int],
             **kwargs: tuple[int, int]) -> tuple[int, int]:
        pass


class AgressorStrategy(GhostStrategy):
    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int],
             **kwargs: tuple[int, int]) -> tuple[int, int]:
        return self._map.next_step_toward(pos, player_pos) \
            or self._map.next_step_toward(pos, self._home) \
            or pos


class AmbusherStrategy(GhostStrategy):
    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int],
             player_dir: tuple[int, int] = (0, 0),
             **kwargs: tuple[int, int]) -> tuple[int, int]:

        tx = player_pos[0] + player_dir[0] * 4
        ty = player_pos[1] + player_dir[1] * 4
        target = (
            max(0, min(self._map.get_width() - 1, tx)),
            max(0, min(self._map.get_height() - 1, ty)),
        )
        return self._map.next_step_toward(pos, target) \
            or self._map.next_step_toward(pos, self._home) \
            or pos


class UnpredictableStrategy(GhostStrategy):
    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int],
             player_dir: tuple[int, int] = (0, 0),
             blinky_pos: tuple[int, int] = (0, 0),
             **kwargs: tuple[int, int]) -> tuple[int, int]:

        pivot_x = player_pos[0] + player_dir[0] * 2
        pivot_y = player_pos[1] + player_dir[1] * 2
        target = (
            max(0, min(self._map.get_width() - 1,
                       2 * pivot_x - blinky_pos[0])),
            max(0, min(self._map.get_height() - 1,
                       2 * pivot_y - blinky_pos[1])),
        )
        return self._map.next_step_toward(pos, target) \
            or self._map.next_step_toward(pos, self._home) \
            or pos


class WandererStrategy(GhostStrategy):
    CHASE_RADIUS: int = 8

    def move(self, pos: tuple[int, int],
             player_pos: tuple[int, int],
             **kwargs: tuple[int, int]) -> tuple[int, int]:

        dist = abs(pos[0] - player_pos[0]) + abs(pos[1] - player_pos[1])
        target = player_pos if dist > self.CHASE_RADIUS else self._home

        return self._map.next_step_toward(pos, target) \
            or self._map.next_step_toward(pos, self._home) \
            or pos
