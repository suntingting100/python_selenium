from calculator import Count
import unittest


class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start")

    def Test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def Test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

    def tearDown(self):
        print("test end")


if __name__ == "__main__":
    # 调用unittest框架的TestSuite()类来构建测试套件(测试集)
    suit = unittest.TestSuite()
    suit.addTest(TestCount("Test_add1"))
    suit.addTest(TestCount("Test_add2"))

    # 执行测试 调用unittest框架的TextTestRunner()类，通过它下面的run()方法来运行suit所组装的测试用例
    runner = unittest.TextTestRunner()
    runner.run(suit)
