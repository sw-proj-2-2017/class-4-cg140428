class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = '_' * len(word)



    def display(self):
        print("Current: ", self.currentStatus)
        print("Tries: ", self.numTries)


    def guess(self, character):
        self.guessedChars.append(character)
        currentStatusList = list(self.currentStatus)
        index = -1
        if character in self.secretWord:
            for letter in self.secretWord:
                index += 1
                if letter in self.guessedChars:
                    currentStatusList[index] = letter
                else:
                    continue
            self.currentStatus = str("".join(currentStatusList))
            return self.currentStatus == self.secretWord
        else:
            self.numTries += 1
            return False
