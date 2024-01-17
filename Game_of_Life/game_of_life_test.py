import unittest
from unittest import TestCase


from game_of_life import evolve

class EvolveTestSuite(TestCase):

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
            "--------------",
            "| ###        |",
            "| #          |",
            "|  #         |",
            "|            |",
            "|            |",
            "--------------"
        ), 5)
        actual = evolve(field, 4)
        self.assertEqual(expected, actual)

    def test_game_world_Warnings(self):
        field = [
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        ]
        with self.assertWarns(Warning):
            evolve(field, 4)
        with self.assertWarns(Warning):
            evolve(tuple(field, -1))
    
    def test_game_world_length(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "| #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertWarns(Warning):
            evolve(field, 2)
    
    def test_game_world_height(self):
        field = (
            "--------------",
            "--------------"
        )
        with self.assertWarns(Warning):
            evolve(field, 3)

if __name__ == "__main__":
    unittest.main()

