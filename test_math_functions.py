import unittest
from math_functions import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(1, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
    #.... indicates that there are four test cases, and each dot represents a test case. In this case, all four tests passed successfully.
#Ran 4 tests in 0.006s tells you that a total of four tests were executed in 0.006 seconds.
#OK at the end indicates that all tests have passed, and your functions are working correctly.