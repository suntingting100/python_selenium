import unittest


# setUpModule和tearDownModule 在整个模块开始和结束时被执行
def setUpModule():
    print("test module start> > > > > >")


def tearDownModule():
    print("test module end> > > > >")


class Test(unittest.TestCase):
    # setUpClass和tearDownClass 在测试类的开始和结束时执行
    @classmethod
    def setUpClass(cls) -> None:
        print("test class start ======>")

    @classmethod
    def tearDownClass(cls) -> None:
        print("test class end =====>")

    # setUp和tearDown 在测试用例的开始和结束时执行
    def setUp(self) -> None:
        print("test case start -- >")

    def tearDown(self) -> None:
        print("test case end -- >")

    def test_case(self):
        print("test case1")

    def test_case2(self):
        print("test case2")


if __name__ == "__main__":
    unittest.main()
    