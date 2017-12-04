import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):


    def setUp(self):
        self.h1 = Hangman()

    def tearDown(self):
        pass

    def testDecreaseLife(self):
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 5)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 4)

    def testCurrentShape(self):
        self.assertEqual(self.h1.text[0], '''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''')
        self.assertEqual(self.h1.text[1],'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\
''')