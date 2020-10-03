import unittest

import pytest

from problems.p5.main import get_prime_factors


class TestProblem5(unittest.TestCase):
    #@pytest.mark.parametrize('test_number', 'expected_factors', )
    def test_get_prime_factors(self):
        for (test_number, expected_factors) in [
        (12, [3, 2, 2]),
        (18, [3, 3, 2]),
        (4, [2, 2]),
        (8, [2, 2, 2]),
        (9, [3, 3]),
        (10, [5, 2]),
    ]:
            ans = get_prime_factors(test_number)
            ans.sort()
            expected_factors.sort()
            # self.assertEqual(len(expected_factors), len(ans))
            self.assertEqual(expected_factors, ans)


if __name__ == '__main__':
    unittest.main()
