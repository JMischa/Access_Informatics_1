__author__ = "Mischa Jampen"
from unittest import TestCase
from task.script import sort



class SortTests(TestCase):
    
    def sorted_iterable_int(self):
        input_data = [1,3,2]
        actual = sort(input_data)
        expected = [1,2,3]
        self.assertEqual(expected, actual)
        self.assertNotEqual(expected, input_data)

    def sorted_iterable_str(self):
        actual = sort(["a", "z", "g"])
        expected = ["a", "g", "z"]
        self.assertEqual(expected ,actual)
    
    def sorted_iterable_float(self):
        actual = sort([1.5, 1.6, 3.0])
        expected = [1.5, 1.6, 3.0]
        self.assertEqual(expected, actual)

    def copy_of_iterable(self):
        actual = sort([1,2,3,4])
        expected = [1,2,3,4]
        self.assertTrue(expected == actual)
    
    def copy_not_same_list(self):
        actual = sort([1,2,3])
        expected = [1,2,3]
        self.assertFalse(expected is actual)
    
    def test_sort_negative_numbers(self):
        input_data = sort([-4, -1, -7, -2, -5])
        expected_result = [-7, -5, -4, -2, -1]
        self.assertEqual(input_data, expected_result)
    
    def test_sort_non_iterable_input(self):
        input_data = sort(42)
        expected_result = None
        self.assertEqual(input_data, expected_result)
    
    def test_sort_none_input(self):
        input_data = sort(None)
        expected_result = None
        self.assertEqual(input_data, expected_result)

    def test_sort_empty_input(self):
        input_data = sort([])
        expected_result = []
        self.assertEqual(input_data, expected_result)
    
    def test_sort_returns_new_list(self):
        input_data = [4, 2, 7, 1, 5]
        result = sort(input_data)
        self.assertNotEqual(result, input_data, "sort should return a new list")