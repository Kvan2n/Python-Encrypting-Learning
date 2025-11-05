from random import randint

def letterToNumber(letter):
    if len(letter) == 1:
        asciinumber = ord(letter)
        return asciinumber - ord("a")
    raise Exception("only one letter at a time, thanks")

def numberToLetter(number):
    number += ord("a")
    asciiletter = chr(number)
    return asciiletter 


def encrypt(key, message):
    splitmessage = list(message)
    splitkey = list(key)
    encryptedList = []
    for i, letter in enumerate(splitmessage):
        currentKey = splitkey[i%len(splitkey)]
        encryptedList.append(str(numberToLetter(letterToNumber(letter)+int(currentKey if currentKey.isdigit() else letterToNumber(currentKey)))))
    return "".join(encryptedList)

def decrypt(key, message):
    splitmessage = list(message)
    splitkey = list(key)
    decryptedList = []
    for i, letter in enumerate(splitmessage):
        currentKey = splitkey[i%len(splitkey)]
        decryptedList.append(str(numberToLetter(letterToNumber(letter)-int(currentKey if currentKey.isdigit() else letterToNumber(currentKey)))))
    return "".join(decryptedList)

def generateKey(length):
    normalSensitivity = 5

    key = ""
    for _ in range(length):
        if randint(1,3) == 1:
            key += str(randint(0,9))
        else:
            random = randint(0, 160)
            while random < 64 and random > 29 or random == 82 or random == 81 or random == 88:
                random = randint(0,160)
            key += numberToLetter(random)

    normals = 0
    for letter in list(key):
        if letter == "a" or letter == "0":
            normals +=1

    if normals > length/normalSensitivity:
        normalCheckList = list(key)
        for i, letter in enumerate(normalCheckList):
            if letter == "a" or letter == "0":
                normalCheckList[i] = numberToLetter(randint(1,26))
        key = "".join(normalCheckList)

    return key

with open("kvankey.key", "r") as file:
    key = file.read()

