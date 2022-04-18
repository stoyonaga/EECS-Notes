import unittest

"""
-	When the highest numbered cylinder with pending request has been serviced, the arm goes to the lowest-numbered
    cylinder with a pending request and continues in an upward direction.
"""


def circular_elevator(head:int, queue:list, control:str) -> list:
    current = queue
    current.append(head)
    current.sort()
    sol = []
    # Set-Up
    start = current.index(head)
    current.remove(head)

    if control == "UP":
        for i in range(0, len(current)):
            sol.append(current[(start + i) % len(current)])
    elif control == "DOWN":
        for i in range(0, len(current)):
            sol.append(current[(start - i - 1) % len(current)])
    return sol


class Solution:
    pass


class TestCircularElevator(unittest.TestCase):
    def test_1up(self):
        input_1 = [1, 36, 16, 34, 9, 12]
        pntr_1 = 11
        sol = circular_elevator(pntr_1, input_1, "UP")
        expected = [12, 16, 34, 36, 1, 9]
        self.assertEqual(sol, expected)

    def test_1down(self):
        input_2 = [1, 36, 16, 34, 9, 12]
        pntr_2 = 11
        sol = circular_elevator(pntr_2, input_2, "DOWN")
        expected = [9, 1, 36, 34, 16, 12]
        self.assertEqual(sol, expected)
