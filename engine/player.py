from .map import Map


class PlayerError(Exception):
    pass


class Player:
    def __init__(self, pos: tuple[int, int], map: Map) -> None:
        self._score = 0
        self._lives = 3

        if not isinstance(map, Map):
            raise ValueError(f"Wrong map type: {map.__class__}")
        self._map = map

        if len(pos) != 2:
            raise PlayerError("Position must have exactly 2 values, "
                              f"got {pos}")
        self.set_position(*pos, map)

        self.set_direction()

    def set_direction(self, direction: tuple[int, int] | None = None) -> None:
        self._direction = direction

    def set_position(self, x: int, y: int, map: Map) -> None:
        mx = map.get_width()
        my = map.get_height()

        try:

            if int(x) > mx - 1:
                raise ValueError

            if int(y) > my - 1:
                raise ValueError

        except ValueError:
            raise PlayerError(f"Invalid player coordinates ({x}, {y}) "
                              f"to map ({mx}, {my})")

        self._position = (x, y)

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

    def add_score(self, points: int) -> None:
        self._score += points

    def add_lives(self, change: int) -> None:
        if not isinstance(change, int):
            raise PlayerError(f"Value {change} not a valid integer number.")

        self._lives += change

    def get_position(self) -> tuple[int, int]:
        return self._position

    def get_direction(self) -> tuple[int, int] | None:
        return self._direction

    def get_score(self) -> int:
        return self._score

    def get_lives(self) -> int:
        return self._lives

    def is_alive(self) -> bool:
        return self._lives > 0
