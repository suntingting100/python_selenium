from is_prime import is_prime
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_case(self):
        self.assertTrue(is_prime(7), msg="Is not prime")

    def tearDown(self) -> None:
        print("test end")


if __name__ == "__main__":
    unittest.main()
