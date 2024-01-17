__author__ = "Mischa Jampen"
import unittest
from unittest import TestCase
from Script import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_move_up(self):
        # NOTE: this test case is buggy and needs fixing!
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_move_left(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left","up")
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    
    def test_move_down(self):
        state = (
            "#####   ",
            "### o  #",
            "#     ##",
            "   #####"
        )
        actual = move(state, "down")
        expected = (
            ("#####   ",
            "###    #",
            "#   o ##",
            "   #####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_invalid_characters(self):
        state = (
            "###e    ",
            "  ## f  ",
            "d# o ###",
            "(     ##"
        )
        with self.assertRaises(Warning):
            move(state, "down")
    
    def test_Invalid_line_size(self):
        state = (
            "     ",
            "##   ",
            "# o ",
            "#####"
        )
        with self.assertRaises(Warning):
            move(state, "left")
    
    def test_more_than_one_player(self):
        state = (
            "####   ",
            "  o ###",
            "#    ##",
            "#o ####"
        )
        with self.assertRaises(Warning):
            move(state, "right")
    
    def test_no_player(self):
        state = (
            "####   ",
            "    ###",
            "#    ##",
            "#  ####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_invalid_world_dimension(self):
        state = (

        )
        with self.assertRaises(Warning):
            move(state, "left")
    
    def test_invalid_world_dimensions_2(self):
        state = (
            "",
            "",
            "",
            ""
        )
        with self.assertRaises(Warning):
            move(state,"right")
    
    def test_possible_move(self):
        state = (
            "#####   ",
            "#####  #",
            "o#######",
            "#  #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")
    
    def test_invalid_move_type(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state,"hello")
    
    def test_same_line_length_1(self):
        state = (
            "o",
            "   ",
            "   ",
            "   ",
            "   ",   
        )
        with self.assertRaises(Warning):
            move(state,"right")
    
if __name__ ==  "__main__":
    unittest.main()