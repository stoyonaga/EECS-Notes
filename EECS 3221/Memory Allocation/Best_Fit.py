import unittest

"""
-	Demonstrates the best fit memory allocation algorithm.
-   Objective: Return a new list of holes, given a process to insert into the available memory.
"""


def best_fit(process: int, hole_queue: list) -> list:
    hole = {}
    for i in range(0, len(hole_queue)):
        if hole_queue[i] >= process:
            hole[hole_queue[i] - process] = i
    if len(hole) == 0:
        raise "Error: No available hole can fit the process size."
    else:
        print("Hole {} is chosen as the candidate.".format(hole_queue[hole[min(hole.keys())]]))
        if process - hole_queue[hole[min(hole.keys())]] == 0:
            print("This will not produce any new hole, since the process perfectly fits the available hole.")
            del hole_queue[hole[min(hole.keys())]]
        else:
            hole_queue[hole[min(hole.keys())]] -= process
            print("This produces a new hole of size {}.".format(hole_queue[hole[min(hole.keys())]]))
        print("Resulting List: {} \n".format(str(hole_queue)))
    return hole_queue


class Solution:
    pass


class TestRecitation(unittest.TestCase):
    def test_best_fit_recitation(self):
        input_1 = [10, 4, 20, 18, 7, 9, 12, 15]
        sol = best_fit(12, input_1)
        expected = [10, 4, 20, 18, 7, 9, 15]
        self.assertEqual(sol, expected)

        sol = best_fit(10, input_1)
        expected = [4, 20, 18, 7, 9, 15]
        self.assertEqual(sol, expected)

        sol = best_fit(9, input_1)
        expected = [4, 20, 18, 7, 15]
        self.assertEqual(sol, expected)

        sol = best_fit(10, input_1)
        expected = [4, 20, 18, 7, 5]
        self.assertEqual(sol, expected)
