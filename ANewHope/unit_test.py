import unittest
import solution

class Basic_unit_tests(unittest.TestCase):

    a_new_hope = solution.ANewHope()

    def custom_test(self, input_data, expected_result):
        self.assertEqual(self.a_new_hope.count(*input_data), expected_result)

    def test001(self):
        first_week = (1,2,3,4)
        last_week = (4,3,2,1)
        D = 3
        self.custom_test((first_week, last_week, D), 4)

    def test002(self):
        first_week = (8,5,4,1,7,6,3,2)
        last_week = (2,4,6,8,1,3,5,7)
        D = 3
        self.custom_test((first_week, last_week, D), 3)

    def test003(self):
        first_week = (1,2,3,4)
        last_week = (1,2,3,4)
        D = 2
        self.custom_test((first_week, last_week, D), 1)

if __name__ == '__main__':
    unittest.main()