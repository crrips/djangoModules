class Intern:

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def __init__(self, name=None) -> None:
        self.name = "My name? I'm nobody, an intern, I have no name." if name is None else name

    def __str__(self) -> str:
        return self.name

    def work(self) -> str:
        raise Exception("I'm just an intern, I can't do that...")

    def coffee(self) -> Coffee:
        return self.Coffee()
            

if __name__ == '__main__':
    intern = Intern()
    print(intern)

    mark = Intern("Mark")
    print(mark)
    
    try:
        print(mark.work())
    except Exception as e:
        print(e)

    print(mark.coffee())

