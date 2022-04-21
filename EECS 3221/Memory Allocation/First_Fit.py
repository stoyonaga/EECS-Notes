import unittest

"""
-	Demonstrates the first fit memory allocation algorithm.
-   Objective: Return a new list of holes, given a process to insert into the available memory.
"""


def first_fit(process: int, hole_queue: list) -> list:
    for i in range(0, len(hole_queue)):
        if process < hole_queue[i]:
            print("Hole {} is chosen as the candidate.".format(hole_queue[i]))
            hole_queue[i] -= process
            print("This produces a new hole of size {}.".format(hole_queue[i]))
            break
        elif process == hole_queue[i]:
            print("Hole {} is chosen as the candidate.".format(hole_queue[i]))
            print("This will not produce any new hole, since the process perfectly fits the available hole.")
            del hole_queue[i]
            break
        elif i == len(hole_queue) - 1:
            raise "Error: No available hole can fit the process size."
    print("Resulting List: {} \n".format(str(hole_queue)))
    return hole_queue


class Solution:
    pass


class TestRecitation(unittest.TestCase):
    def test_first_fit_recitation(self):
        input_1 = [10, 4, 20, 18, 7, 9, 12, 15]
        sol = first_fit(12, input_1)
        expected = [10, 4, 8, 18, 7, 9, 12, 15]
        self.assertEqual(sol, expected)

        sol = first_fit(10, input_1)
        expected = [4, 8, 18, 7, 9, 12, 15]
        self.assertEqual(sol, expected)

        sol = first_fit(9, input_1)
        expected = [4, 8, 9, 7, 9, 12, 15]
        self.assertEqual(sol, expected)
