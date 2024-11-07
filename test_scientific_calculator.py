import unittest
import math
from scientific_calculator import (
    asin_function, acos_function, sinh_function, cosh_function, exp_function,
    sin_function, tanh_function, cos_function, tan_function, sqrt_function, atan_function, log_function,
    asin_function, acos_function, sinh_function, cosh_function, exp_function
)

class TestScientificCalculator(unittest.TestCase):

 # Tests for asin function
    def asin_positive(self):
        self.assertAlmostEqual(asin_function(1), math.asin(1))

    def asin_negative(self):
        self.assertAlmostEqual(asin_function(-1), math.asin(-1))

    def asin_invalid(self):
        with self.assertRaises(ValueError):
            asin_function(2)

    def asin_non_numeric(self):
        with self.assertRaises(ValueError):
            asin_function("hello")

# Tests for acos function
    def acos_positive(self):
        self.assertAlmostEqual(acos_function(1), math.acos(1))

    def acos_negative(self):
        self.assertAlmostEqual(acos_function(-1), math.acos(-1))

    def acos_invalid(self):
        with self.assertRaises(ValueError):
            acos_function(2)

    def acos_non_numeric(self):
        with self.assertRaises(ValueError):
            acos_function("hello")

            # Tests for sinh function
    def sinh_positive(self):
        self.assertAlmostEqual(sinh_function(1), math.sinh(1))

    def sinh_negative(self):
        self.assertAlmostEqual(sinh_function(-1), math.sinh(-1))

    def sinh_non_numeric(self):
        with self.assertRaises(ValueError):
            sinh_function("hello")

     # Tests for cosh function
    def cosh_positive(self):
        self.assertAlmostEqual(cosh_function(1), math.cosh(1))

    def cosh_negative(self):
        self.assertAlmostEqual(cosh_function(-1), math.cosh(-1))

    def cosh_non_numeric(self):
        with self.assertRaises(ValueError):
            cosh_function("hello")

    # Tests for exp function
    def exp(self):
        self.assertEqual(exp_function(1), math.exp(1))

    def exp_non_numeric(self):
        with self.assertRaises(ValueError):
            exp_function("hello")


    # Tests for sin function
    def sin_positive(self):
        self.assertAlmostEqual(sin_function(90), math.sin(math.radians(90)))

    def sin_negative(self):
        self.assertAlmostEqual(sin_function(-90), math.sin(math.radians(-90)))

    def sin_zero(self):
        self.assertAlmostEqual(sin_function(0), math.sin(0))

    def sin_non_numeric(self):
        with self.assertRaises(ValueError):
            sin_function("hello")

    # Tests for cos function
    def cos_positive(self):
        self.assertAlmostEqual(cos_function(90), math.cos(math.radians(90)))

    def cos_negative(self):
        self.assertAlmostEqual(cos_function(-90), math.cos(math.radians(-90)))

    def cos_zero(self):
        self.assertAlmostEqual(cos_function(0), math.cos(0))

    def cos_non_numeric(self):
        with self.assertRaises(ValueError):
            cos_function("hello")

    # Tests for tan function
    def tan_positive(self):
        self.assertAlmostEqual(tan_function(45), math.tan(math.radians(45)))

    def test_tan_non_numeric(self):
        with self.assertRaises(ValueError):
            tan_function("hello")

    # Tests for sqrt function
    def sqrt_positive(self):
        self.assertEqual(sqrt_function(16), math.sqrt(16))

    def sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt_function(-16)

    def sqrt_non_numeric(self):
        with self.assertRaises(ValueError):
            sqrt_function("hello")

    # Tests for log function
    def log_positive(self):
        self.assertEqual(log_function(10), math.log(10))

    def log_non_numeric(self):
        with self.assertRaises(ValueError):
            log_function("hello")

    def log_negative(self):
        with self.assertRaises(ValueError):
            log_function(-10)


    # Tests for atan function
    def atan_positive(self):
        self.assertAlmostEqual(atan_function(1), math.atan(1))

    def atan_negative(self):
        self.assertAlmostEqual(atan_function(-1), math.atan(-1))

    def atan_non_numeric(self):
        with self.assertRaises(ValueError):
            atan_function("hello")

    

    # Tests for tanh function
    def tanh_positive(self):
        self.assertAlmostEqual(tanh_function(1), math.tanh(1))

    def tanh_negative(self):
        self.assertAlmostEqual(tanh_function(-1), math.tanh(-1))

    def tanh_non_numeric(self):
        with self.assertRaises(ValueError):
            tanh_function("hello")

if __name__ == '__main__':
    unittest.main()