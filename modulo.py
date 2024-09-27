import unittest

def modulo(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return dividend % divisor

class TestModuloFunction(unittest.TestCase):
    def test_modulo_correct_cases(self):
        self.assertEqual(modulo(10, 3), 2)
        self.assertEqual(modulo(20, 5), 4)
        self.assertEqual(modulo(7, -3), -2)
        self.assertEqual(modulo(-7, 3), 2)
        self.assertEqual(modulo(12, 3), 0)

    def test_modulo_division_by_zero(self):
        with self.assertRaises(ValueError) as e:
            modulo(10, 0)
        self.assertEqual(str(e.exception), "Division by zero is not allowed.")

if __name__ == '__main__':
    unittest.main()