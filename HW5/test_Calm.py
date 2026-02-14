import unittest
from Calm import Calm

class MyTestCase(unittest.TestCase):
    def test_repr(self):
        calm = Calm()
        self.assertEqual(repr(calm),"Calm")  # add assertion here

    def test_get_patience_factor1(self):
        calm = Calm()
        self.assertEqual(calm.get_patience_factor(10),2.21)

    def test_get_patience_factor2(self):
        calm = Calm()
        self.assertEqual(calm.get_patience_factor(30), 2.68)

if __name__ == '__main__':
    unittest.main()
