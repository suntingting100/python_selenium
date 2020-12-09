from calculator import Count
import unittest


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        print("test start")

    def tearDown(self) -> None:
        print("test end")


class TestAdd(MyTest):

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)


class TestSub(MyTest):

    def test_sub1(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)


if __name__ == "__main__":
    unittest.main()
