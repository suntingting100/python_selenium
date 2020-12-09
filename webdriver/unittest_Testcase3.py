from calculator import Count
import unittest


class TestAdd(unittest.TestCase):

    def setUp(self) -> None:
        print("test start")

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

    def tearDown(self) -> None:
        print("test end")


class TestSub(unittest.TestCase):

    def setUp(self) -> None:
        print("test start")

    def test_sub1(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)

    def tearDown(self) -> None:
        print("test end")


if __name__ == "__main__":
    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add1"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub1"))
    suite.addTest(TestSub("test_sub2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
