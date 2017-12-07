import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):


    def setUp(self):
        self.h1 = Hangman()

    def tearDown(self):
        pass

    def testDecreaseLife(self):
        self.assertEqual(self.h1.remainingLives, 6)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 5)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 4)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 3)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 2)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 1)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 0)

    def testCurrentShape(self):
        self.assertEqual(self.h1.currentShape(), self.h1.text[0])
        self.assertEqual(self.h1.currentShape(), self.h1.text[1])
        self.assertEqual(self.h1.currentShape(), self.h1.text[2])
        self.assertEqual(self.h1.currentShape(), self.h1.text[3])
        self.assertEqual(self.h1.currentShape(), self.h1.text[4])
        self.assertEqual(self.h1.currentShape(), self.h1.text[5])
        self.assertEqual(self.h1.currentShape(), self.h1.text[6])

if __name__ == '__main__':
    unittest.main()
