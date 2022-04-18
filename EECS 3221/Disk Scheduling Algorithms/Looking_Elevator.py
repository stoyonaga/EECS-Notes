import unittest

"""
-	This version requires the software to maintain 1 bit, representing the current direction (UP, DOWN)
-	The arm keeps moving in the same direction until reaching the end of the disk. This is when the direction is reversed.
-	Still favours requests in the middle, but does not starve requests
"""


def elevator(head: int, queue: list, control: str) -> list:
    current = queue
    current.append(head)
    current.sort()

    seg1 = []
    seg2 = []

    start = current.index(head)
    current.remove(head)

    if control == "UP":
        for i in range(0, len(current)):
            if i < len(current):
                if start + i < len(current):
                    seg1.append(current[(start + i)])
                else:
                    seg2.append(current[((start + i) % len(current))])
        seg2.reverse()
        return seg1 + seg2
    if control == "DOWN":
        for i in range(0, start):
            seg1.append(current[i])
        for i in range(start, len(current)):
            seg2.append(current[i])
        seg1.reverse()
        return seg1 + seg2


class Solution:
    pass


class TestElevator(unittest.TestCase):
    def test_elevator1a(self):
        input_1 = [1, 36, 16, 34, 9, 12]
        pntr_1 = 11
        sol = elevator(pntr_1, input_1, "UP")
        expected = [12, 16, 34, 36, 9, 1]
        self.assertEqual(sol, expected)

    def test_elevator1b(self):
        input_2 = [1, 36, 16, 34, 9, 12]
        pntr_2 = 11
        sol = elevator(pntr_2, input_2, "DOWN")
        expected = [9, 1, 12, 16, 34, 36]
        self.assertEqual(sol, expected)

    def test_elevator2a(self):
        input_3 = [10, 22, 20, 2, 40, 6, 38]
        pntr_3 = 20
        sol = elevator(pntr_3, input_3, "UP")
        expected = [20, 22, 38, 40, 10, 6, 2]
        self.assertEqual(sol, expected)

    def test_elevator2b(self):
        input_4 = [10, 22, 20, 2, 40, 6, 38]
        pntr_4 = 20
        sol = elevator(pntr_4, input_4, "DOWN")
        expected = [10, 6, 2, 20, 22, 38, 40]
        self.assertEqual(sol, expected)
