import random
import sys

inputValue = sys.argv[0]


def getSentence(amountOfWords):
    wordList = getWordList()
    mySentence = ""
    for i in range(0, int(amountOfWords)):
        randomWord = wordList[random.randint(0, len(wordList))]
        mySentence = mySentence + " " + randomWord
    return mySentence


def getWordList():
    wordFile = open("test words.txt", "r")
    wordList = wordFile.read().strip().split("\n")
    wordFile.close()
    return wordList

if __name__ == '__main__':
    print(getSentence(5))
