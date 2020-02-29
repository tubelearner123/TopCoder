import unittest
import ABBADiv1

class Basic_unit_tests(unittest.TestCase):

    p = 'Possible'
    ip = 'Impossible'

    abba_div1 = ABBADiv1.ABBADiv1()

    def custom_test(self, input_data, expected_result):
        self.assertEqual(self.abba_div1.canObtain(*input_data), expected_result)

    def test001(self):
        self.custom_test(('BAAAAABAA', 'BAABAAAAAB'), self.p)

    def test002(self):
        self.custom_test(('A', 'ABBA'), self.ip)

    def test003(self):   
        self.custom_test(('AAABBAABB', 'BAABAAABAABAABBBAAAAAABBAABBBBBBBABB'), self.p)

    def test004(self):
        self.custom_test(('AAABAAABB', 'BAABAAABAABAABBBAAAAAABBAABBBBBBBABB'), self.ip)

if __name__ == '__main__':
    unittest.main()