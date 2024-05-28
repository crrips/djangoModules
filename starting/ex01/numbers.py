def openFile(filename: str) -> str:
    f = open(filename, "r")
    return f


if __name__ == '__main__':
    numbers = openFile("numbers.txt").read()
    for i in numbers.split(","):
        if i.find("\n"):
            i = i.replace("\n", "")
        print(i)
