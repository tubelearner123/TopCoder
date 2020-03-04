import unittest
import solution

class Basic_unit_tests(unittest.TestCase):

    access_changer = solution.AccessChanger()

    def custom_test(self, input_data, expected_result):
        self.assertEqual(self.access_changer.convert(input_data), expected_result)

    def test001(self):
        program = ("Test* t = new Test();", "t->a = 1;", "t->b = 2;", "t->go(); // a=1, b=2 --> a=2, b=3", )
        expected_output = ("Test* t = new Test();", "t.a = 1;", "t.b = 2;", "t.go(); // a=1, b=2 --> a=2, b=3", )
        self.custom_test(program, expected_output)

    def test002(self):
        program = ("---> // the arrow --->", "---", "> // the parted arrow", )
        expected_output = ("--. // the arrow --->", "---", "> // the parted arrow", )
        self.custom_test(program, expected_output)

    def test003(self):
        program = ("->-> // two successive arrows ->->", )
        expected_output = (".. // two successive arrows ->->", )
        self.custom_test(program, expected_output)

if __name__ == '__main__':
    unittest.main()