from homemadeEncryption import generateKey

def makeKeyToFile(length, filename):
    with open(filename, "w") as file:
        file.write(generateKey(length))

if __name__ == "__main__":
    filename=input("Filename:\n")
    length=input("Length:\n")
    if length.isdigit():
        makeKeyToFile(filename=filename, length=int(length))
        print("Success")
    else:
        raise Exception("Length must be a number")