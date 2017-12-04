import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u l t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')
        self.g1.guess('c')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a e l n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e l n t u ')
        self.g1.guess('c')
        self.assertEqual(self.g1.displayGuessed(), ' a c d e l n t u ')

    def testGuess(self, character):
        self.g1.guess('a')
        self.assertTrue(self.g1.guess())
        self.g1.guess('t')
        self.assertTrue(self.g1.guess())
        self.g1.guess('u')
        self.assertTrue(self.g1.guess())
        self.g1.guess('l')
        self.assertTrue(self.g1.guess())
        self.g1.guess('d')
        self.assertTrue(self.g1.guess())
        self.g1.guess('c')
        self.assertFalse(self.g1.guess())
if __name__ == '__main__':
    unittest.main()
