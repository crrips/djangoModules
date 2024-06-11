import sys, os, settings


if __name__ == '__main__':
    if sys.argv.__len__() != 2:
        print("usage: render.py <file>")
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print("file not found")
        sys.exit(1)
    if (sys.argv[1].split(".")[-1] != "template"):
        print("file is not a template")
        sys.exit(1)

    f = open(sys.argv[1], 'r')
    template = f.read()
    f.close()

    file = template.format(name=settings.name, surname=settings.surname, age=settings.age, profession=settings.profession)

    f = open(sys.argv[1].split(".")[0] + ".html", 'w')
    f.write(file)
    f.close()
