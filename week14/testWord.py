import unittest

from word import Word

class TestWord(unittest.TestCase):


    def setUp(self):
        self.w1 = Word('words.txt')


    def tearDown(self):
        pass

    def testTest(self):
        self.assertIn(self.w1.test(), self.w1.words)


    def testRandFromDB(self):
        self.assertIn(self.w1.randFromDB(), self.w1.words)



if __name__ == '__main__':
    unittest.main()

