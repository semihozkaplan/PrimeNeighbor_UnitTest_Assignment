'''
Tested by Semih Özkaplan
'''
import unittest
import src.primeNeighbor as pn

class PrimeNeighborTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test010(self):
        actualResult = pn.primeNeighbor(upperBound=2)
        expectedResult = 2
        self.assertEqual(expectedResult, actualResult)

    def test_previous_prime_non_prime(self):
        actualResult = pn.primeNeighbor(upperBound=50)
        expectedResult = 47
        self.assertEqual(expectedResult, actualResult)

    def test_previous_prime_large_non_prime(self):
        actualResult = pn.primeNeighbor(upperBound=1000)
        expectedResult = 997
        self.assertEqual(expectedResult, actualResult)

    def test_return_same_prime(self):
        actualResult = pn.primeNeighbor(upperBound=73)
        expectedResult = 73
        self.assertEqual(expectedResult, actualResult)

    def test_zero_for_float(self):
        actualResult = pn.primeNeighbor(upperBound=99.9)
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test_zero_for_string(self):
        actualResult = pn.primeNeighbor(upperBound="Semih")
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test_zero_for_negative(self):
        actualResult = pn.primeNeighbor(upperBound=-7)
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)

    def test_previous_prime_small_prime(self):
        actualResult = pn.primeNeighbor(upperBound=4)
        expectedResult = 3
        self.assertEqual(expectedResult, actualResult)

    def test_return_same_largest_prime(self):
        actualResult = pn.primeNeighbor(upperBound=997)
        expectedResult = 997
        self.assertEqual(expectedResult, actualResult)

    def test_previous_prime_medium_non_prime(self):
        actualResult = pn.primeNeighbor(upperBound=996)
        expectedResult = 991
        self.assertEqual(expectedResult, actualResult)

    def test_return_same_small_prime(self):
        actualResult = pn.primeNeighbor(upperBound=3)
        expectedResult = 3
        self.assertEqual(expectedResult, actualResult)

    def test_high_value_than_bound(self):
        actualResult = pn.primeNeighbor(upperBound=2000)
        expectedResult = 0
        self.assertEqual(expectedResult, actualResult)



