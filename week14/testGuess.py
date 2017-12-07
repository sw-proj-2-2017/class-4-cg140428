import unittest

from guess import Guess

class TestGuess(unittest.TestCase):


    def setUp(self):
        self.g1 = Guess('default')


    def tearDown(self):
        pass


    def testGuess(self):
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('a')
        # self.assertEqual(self.guessedChars, {'', 'a', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertTrue(self.g1.guess('a'))
        self.g1.guess('t')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.assertTrue(self.g1.guess('t'))
        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.assertTrue(self.g1.guess('u'))
        self.g1.guess('l')
        self.assertEqual(self.g1.currentStatus, '_e_ault')
        self.assertTrue(self.g1.guess('l'))
        self.g1.guess('d')
        self.assertEqual(self.g1.currentStatus, 'de_ault')
        self.assertTrue(self.g1.guess('d'))
        # secretWord에 없는 문자
        self.g1.guess('c')
        self.assertEqual(self.g1.currentStatus, 'de_ault')
        self.assertFalse(self.g1.guess('c'))
        # 알파벳이 아닌 문자
        self.g1.guess('!')
        self.assertEqual(self.g1.currentStatus, 'de_ault')
        self.assertFalse(self.g1.guess('!'))
        self.g1.guess('ㄱ')
        self.assertEqual(self.g1.currentStatus, 'de_ault')
        self.assertFalse(self.g1.guess('ㄱ'))
        self.g1.guess('8')
        self.assertEqual(self.g1.currentStatus, 'de_ault')
        self.assertFalse(self.g1.guess('8'))



    def testFinished(self):
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('!')
        self.assertFalse(self.g1.finished())
        #secretWord에 없는 문자
        self.g1.guess('c')
        self.assertFalse(self.g1.finished())
        #알파벳이 아닌 문자
        self.g1.guess('!')
        self.assertFalse(self.g1.finished())
        self.g1.guess('ㄱ')
        self.assertFalse(self.g1.finished())
        self.g1.guess('8')
        self.assertFalse(self.g1.finished())
        #currentStatus == secretWord 일 때
        self.g1.guess('f')
        self.assertTrue(self.g1.finished())


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
        #secretWord에 없는 문자
        self.g1.guess('c')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')
        #알파벳이 아닌 문자
        self.g1.guess('!')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')
        self.g1.guess('ㄱ')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')
        self.g1.guess('8')
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
        #secretWord에 없는 문자
        self.g1.guess('c')
        self.assertEqual(self.g1.displayGuessed(), ' a c d e l n t u ')
        #알파벳이 아닌 문자
        self.g1.guess('!')
        self.assertEqual(self.g1.displayGuessed(), ' ! a c d e l n t u ')
        self.g1.guess('ㄱ')
        self.assertEqual(self.g1.displayGuessed(), ' ! a c d e l n t u ㄱ ')
        self.g1.guess('8')
        self.assertEqual(self.g1.displayGuessed(), ' ! 8 a c d e l n t u ㄱ ')

if __name__ == '__main__':
    unittest.main()
