import unittest
from Calm import Calm
from Explosive import Explosive
from Furious import Furious
from TypeA import TypeA


class MyTestCase(unittest.TestCase):
    def test_adjust_mood1(self):
        personality = TypeA()
        mood = personality.adjust_mood(Explosive(),50)
        self.assertTrue(isinstance(mood,Explosive))  # add assertion here

    def test_adjust_mood2(self):
        personality = TypeA()
        mood = personality.adjust_mood(Calm(), 32)
        self.assertTrue(isinstance(mood,Furious))  # add assertion here

    def test_repr(self):
        personality = TypeA()
        self.assertEqual("TypeA",repr(personality))

if __name__ == '__main__':
    unittest.main()
