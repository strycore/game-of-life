class World(object):
    def __init__(self, seed):
        self.cells = seed

    def cell_at(self, position):
        return position in self.cells

    def _iter_cells(self, position):
        for x in range(-1, 2):
            for y in range(-1, 2):
                yield (position[0] + x, position[1] + y)

    def neighbors_at(self, position):
        neighbors = set()
        for cell in self._iter_cells(position):
            if self.cell_at(cell) and cell != position:
                neighbors.add(cell)
        return neighbors

    def cell_lives(self, position):
        if position in self.cells:
            return len(self.neighbors_at(position)) in (2, 3)
        else:
            return len(self.neighbors_at(position)) == 3

    def tick(self):
        next_cells = set()
        for position in self.cells:
            for cell in self._iter_cells(position):
                if self.cell_lives(cell):
                    next_cells.add(cell)
        self.cells = next_cells
