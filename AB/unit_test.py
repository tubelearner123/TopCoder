import unittest
import AB

class Basic_unit_tests(unittest.TestCase):

    ab = AB.AB()

    def custom_test(self, input_data, expected_result):
        self.assertEqual(self.ab.createString(*input_data), expected_result)

    def test001(self):
        self.custom_test((3, 2), 'ABB')

    def test002(self):
        self.custom_test((2, 0), 'BA')

    def test003(self):
        self.custom_test((5, 8), '')

    def test004(self):
        self.custom_test((10, 12), 'BAABBABAAB')

    # def test005(self):
    #     self.custom_test([4096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], self.p)

    # def test006(self):
    #     self.custom_test([4096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], self.p)

    # def test007(self):
    #     self.custom_test([4096, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], self.p)

    # def test008(self):
    #     self.custom_test([4097, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], self.p)

    # def test009(self):
    #     self.custom_test([2048, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], self.p)

    # def test010(self):
    #     self.custom_test([2048, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], self.p)

    # def test011(self):
    #     self.custom_test([2048, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], self.p)

    # def test012(self):
    #     self.custom_test([2047, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], self.p)

    # def test013(self):
    #     self.custom_test([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], self.ip)

    # def test014(self):
    #     self.custom_test([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1048575], self.ip)

    # def test015(self):
    #     self.custom_test([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1048576], self.p)

    # def test016(self):
    #     self.custom_test([0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3], self.ip)

    # def test017(self):
    #     self.custom_test([0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 4], self.p)

    # def test018(self):
    #     self.custom_test([1], self.p)

    # def test019(self):
    #     self.custom_test([0], self.ip)

    # def test020(self):
    #     self.custom_test([0, 1, 2], self.p)

    # def test021(self):
    #     self.custom_test([0, 3], self.p)

    # def test022(self):
    #     self.custom_test([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], self.p)

    # def test023(self):
    #     self.custom_test([0, 0, 0, 0, 15], self.ip)

    # def test024(self):
    #     self.custom_test([0, 1, 1, 3], self.p)

    # def test025(self):
    #     self.custom_test([0, 0, 0, 0, 16], self.p)

    # def test026(self):
    #     self.custom_test([1, 0, 0, 0, 0], self.p)

    # def test027(self):
    #     self.custom_test([0, 0, 2, 0, 0, 0, 0, 0, 0, 0], self.ip)

    # def test028(self):
    #     self.custom_test([0, 1, 0, 4], self.p)

    # def test029(self):
    #     self.custom_test([0, 2, 0, 0], self.p)

    # def test030(self):
    #     self.custom_test([0, 1], self.ip)

    # def test031(self):
    #     self.custom_test([0, 0, 0, 0, 0, 32], self.p)

if __name__ == '__main__':
    unittest.main()