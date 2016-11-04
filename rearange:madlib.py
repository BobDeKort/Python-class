import random
import sys

inputAsList = sys.argv
inputAsList.remove(inputAsList[0])
inputAsString = " ".join(inputAsList)


def rearrange_list(inputList):
    result = ""
    for i in range(0, len(inputList)):
        randomNum = getRandomIndex(len(inputList))
        word = inputList[randomNum]
        result = result + (word + " ")
        inputList.remove(inputList[randomNum])

    return result


def getRandomIndex(listRange):
    return random.randrange(0, listRange)


def reverse_string(string):
    return string[::-1]


def madlib():
    adjective = raw_input("give me an adjective: ")
    noun = raw_input("give me a noun: ")
    animal = raw_input("Give me an animal: ")
    sound = raw_input("Give me a sound: ")

    result = str.title(adjective) + " Macdonald had a " + noun + ", E-I-E-I-O \n and on that " + noun + " he had an " + animal + ", E-I-E-I-O \n with a " + sound + " " + sound + " here \n and a " + \
        sound + " " + sound + " there,\n here a " + sound + ", there a " + sound + ",\n everywhere a " + \
        sound + " " + sound + ",\n " + adjective + \
        " Macdonald had a Smoke Detector, E-I-E-I-O."

    return result


if __name__ == '__main__':
    # print(madlib())
    print(rearrange_list(inputAsList))
