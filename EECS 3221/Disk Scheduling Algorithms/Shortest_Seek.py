import unittest
import sys

"""
This algorithm works by always handling the closest request next, to minimize seek time.
This is to say that it uses the greedy algorithm to handle the closest next request to minimize the seek time.

Precondition: requests must be a non-empty list
"""


def shortest_seek(current: int, requests: list) -> list:
    if len(requests) > 2:
        requests.insert(0, current)
        current_head = current
        rm_elem = None
        sol = []
        for i in range(0, len(requests)):
            shortest_dx = sys.maxsize
            for elem in requests:
                if 0 < current_head - elem < shortest_dx:
                    shortest_dx = current_head - elem
                    rm_elem = elem
                elif 0 < elem - current_head < shortest_dx:
                    shortest_dx = elem - current_head
                    rm_elem = elem
            sol.append(requests[requests.index(current_head)])
            del requests[requests.index(current_head)]
            current_head = rm_elem
        del sol[0]
        return sol
    else:
        return requests


class Solution:
    pass


class TestSeek(unittest.TestCase):
    def test_lecture(self):
        sol = shortest_seek(11, [1, 36, 16, 34, 9, 12])
        expected = [12, 9, 16, 1, 34, 36]
        self.assertEqual(sol, expected)

    def test_homework(self):
        sol = shortest_seek(20, [10, 22, 20, 2, 40, 6, 38])
        expected = [22, 20, 10, 6, 2, 38, 40]
        self.assertEqual(sol, expected)

    def test_recitation(self):
        sol = shortest_seek(50, [20, 250, 220, 190, 60])
        expected = [60, 20, 190, 220, 250]
        self.assertEqual(sol, expected)
