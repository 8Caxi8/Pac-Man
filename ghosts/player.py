from .map import Map


class Player:
    def __init__(self, pos: tuple[int, int], map: Map) -> None:
        self._score = 0
        self._map = map
        self._position = pos
        self.set_direction()

    def set_direction(self, direction: tuple[int, int] | None = None) -> None:
        self._direction = direction

    def move(self) -> None:
        if not self._direction:
            return

        neighbors = self._map.neighbors(self._position)
        target = (
            self._position[0] + self._direction[0],
            self._position[1] + self._direction[1],
        )

        if target not in neighbors:
            self.set_direction()
            return

        self._position = target

    def get_position(self) -> tuple[int, int]:
        return self._position

    def add_score(self, points: int) -> None:
        self._score += points

    def get_direction(self) -> tuple[int, int] | None:
        return self._direction

    def get_score(self) -> int:
        return self._score
