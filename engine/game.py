class World(object):
    def __init__(self, seed):
        self.cells = seed

    def cell_at(self, position):
        return position in self.cells

    def _iter_neighbors(self, position):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) == (0, 0):
                    continue
                yield (position[0] + x, position[1] + y)

    def neighbors_at(self, position):
        neighbors = set()
        for cell in self._iter_neighbors(position):
            if self.cell_at(cell):
                neighbors.add(cell)
        return neighbors

    def cell_lives(self, position):
        return len(self.neighbors_at(position)) in (2, 3)
