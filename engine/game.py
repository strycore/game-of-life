class World(object):
    def __init__(self, seed):
        self.cells = seed

    def cell_at(self, position):
        return position in self.cells

    def neighbors_at(self, position):
        neighbors = set()
        for x in range(-1, 2):
            for y in range(-1, 2):
                cell = (position[0] + x, position[1] + y)
                if self.cell_at(cell):
                    neighbors.add(cell)
        return neighbors
