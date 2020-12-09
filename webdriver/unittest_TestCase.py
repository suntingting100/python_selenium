from calculator import Count
import unittest


# 创建TestCount类继承unittest的TestCase
class TestCount(unittest.TestCase):

    def setUp(self):  # setUp()方法用于测试用例执行前的初始化工作
        print("test start")

    def test_add(self):
        j = Count(2, 3)  # 调用Count类并传入要计算的数
        # 通过调用uinttest框架所提供的assertEqual()方法对add()返回值进行断言，判断两是否相等，assertEqual()方法由TestCase类继承来
        self.assertEqual(j.add(), 5)  # 通过调用add()方法得两数相加的返回值

    def tearDown(self):  # tearDown()方法用于测试用例执行后的善后工作
        print("test end")


# 当直接运行的时候，if __name__ == "__main__":下面的执行，
# 当被导入的时候，if __name__ == "__main__":下面的不执行
if __name__ == "__main__":
    # main()方法使用Testloader类来搜索所有包含在该模块中以"test"命名开头的测试方法，并自动执行他们
    unittest.main()
