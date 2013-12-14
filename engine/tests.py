from unittest import TestCase
from game import World


class TestWorldMechanics(TestCase):
    def test_can_set_initial_state(self):
        seed = set([(1, 2), (2, 3), (5, 7)])
        world = World(seed)
        self.assertTrue(world.cell_at((1, 2)))
        self.assertFalse(world.cell_at((1, 7)))

    def test_can_count_neighbors(self):
        world = World(set([(1, 1), (2, 1), (1, 2), (2, 2), (5, 5)]))
        self.assertEqual(len(world.neighbors_at((1, 1))), 4)


class TestCellState(TestCase):
    pass
