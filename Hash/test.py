#mission: convert any length string into a fixed length string that can be verified

def makeHash(input):
    splitInput = list(input)
    hash = []
    for i in range(100):
        hash.append(splitInput[i % len(splitInput)])
    return "".join(hash)

print(makeHash("test"))