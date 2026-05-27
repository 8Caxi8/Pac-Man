from collections import deque


class Map:
    N: int = 0
    E: int = 1
    S: int = 2
    W: int = 3

    DIRS: list[tuple[int, int, int]] = [
        (0, -1, N),
        (1,  0, E),
        (0,  1, S),
        (-1, 0, W),
    ]

    def __init__(self, maze: list[list[int]], width: int, height: int) -> None:
        self._maze = maze
        self._width = width
        self._height = height

    def next_step_toward(self,
                         pos: tuple[int, int],
                         target: tuple[int, int]) -> tuple[int, int] | None:
        if pos == target:
            return pos

        queue: deque[tuple[int, int]] = deque([pos])
        visited: set[tuple[int, int]] = {pos}
        parent: dict[tuple[int, int], tuple[int, int] | None] = {pos: None}

        while queue:
            cell = queue.popleft()

            if cell == target:
                path: list[tuple[int, int]] = []
                current: tuple[int, int] | None = cell
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[-2] if len(path) > 1 else None

            for neighbor in self.neighbors(cell):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = cell
                    queue.append(neighbor)

        return None

    def is_wall(self, pos: tuple[int, int], direction: int) -> bool:
        x, y = pos
        return bool(self._maze[y][x] & (1 << direction))

    def in_bounds(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        return 0 <= x < self._width and 0 <= y < self._height

    def neighbors(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        result = []
        for dx, dy, direction in self.DIRS:
            nx, ny = dx + pos[0], dy + pos[1]
            if self.in_bounds((nx, ny)) and not self.is_wall(pos, direction):
                result.append((nx, ny))
        return result
