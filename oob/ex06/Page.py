from elements import *

class Page:
    def __init__(self, elem: Elem) :
        if not isinstance(elem, Elem):
            raise Elem.Error()
        self.elem = elem

    def __str__(self):
        return self.elem.__str__()

    def is_valid(self) -> bool:
        if not isinstance(self.elem, Html):
            return False
        return self.__is_valid(self.elem)

    def __is_valid(self, elem: Elem) -> bool:
        if not isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)):
            return False
        if isinstance(elem, Html) and len(elem.content) == 2 and type(elem.content[0]) == Head and type(elem.content[1]) == Body:
            if (all(self.__is_valid(el) for el in elem.content)):
                return True
        elif isinstance(elem, Head) and [isinstance(el, Title) for el in elem.content].count(True) == 1:
            if (all(self.__is_valid(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Body, Div)) and all([isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for el in elem.content]):
            if (all(self.__is_valid(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Title, H1, H2, Li, Th, Td)) and len(elem.content) == 1 and type(elem.content[0]) == Text:
            return True
        elif isinstance(elem, P) and all([isinstance(el, Text) for el in elem.content]):
            return True
        elif isinstance(elem, Span) and all([isinstance(el, (Text, P)) for el in elem.content]):
            if (all(self.__is_valid(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Ul, Ol)) and all([isinstance(el, Li) for el in elem.content]):
            if (all(self.__is_valid(el) for el in elem.content)):
                return True
        elif isinstance(elem, Tr) and all([isinstance(el, (Th, Td)) for el in elem.content]) and all(type(el) == type(elem.content[0]) for el in elem.content):
            if (all(self.__is_valid(el) for el in elem.content)):
                return True
        elif isinstance(elem, Table) and all([isinstance(el, Tr) for el in elem.content]):
            if (all(self.__is_valid(el) for el in elem.content)):
                return True
        return False

    def check(self) -> bool:
        red = "\033[31m"
        green = "\033[32m"
        end = "\033[0m"

        res = self.is_valid()
        if res == False:
            print(f"{red}TEST FAILED{end}")
            return False
        else:
            print(f"{green}TEST PASSED{end}")
            return True

    def write_to_file(self, file_name="page.html"):
        if self.check() and file_name[-5:] == ".html":
            print(self)

            f = open(file_name, "w")
            f.write(str(self))
            f.close()
        else:
            print("Error: Invalid page")


def test(page1: Page, page2: Page):
    print("\n")
    page = page1
    page.check()
    print(page)
    print("=================================")
    page = page2
    page.check()
    print(page)
    

def test_head_body():
    page1 = Page(Html([Head(Title(Text("aboba"))), Body()]))
    page2 = Page(Html([Head(Title(Text("aboba"))), Body(), Body()]))
    test(page1, page2)


def test_title():
    page1 = Page(Html([Head(Title(Text("aboba"))), Body()]))
    page2 = Page(Html([Head([Title(Text("aboba")), Title(Text("aboba2"))]), Body()]))
    test(page1, page2)


def test_body():
    page1 = Page(Html([Head(Title(Text("aboba"))), Body([H1(Text("aboba"))])]))
    page2 = Page(Html([Head(Title(Text("aboba"))), Body([Img('src="http://i.imgur.com/pfp3T.jpg"')])]))
    test(page1, page2)


def test_text():
    page1 = Page(Html([Head(Title(Text("aboba"))), Body([H1(Text("aboba"))])]))
    page2 = Page(Html([Head(Title(Text("aboba"))), Body([H1("aboba")])]))
    test(page1, page2)


def test_span():
    page1 = Page(Html([Head(Title(Text("aboba"))), Body([Span([P(Text("aboba"))])])]))
    page2 = Page(Html([Head(Title(Text("aboba"))), Body([Span([Img('src="http://i.imgur.com/pfp3T.jpg"')])])]))
    test(page1, page2)


def test_list():
    page1 = Page(Html([Head(Title(Text("aboba"))), Body([Ul([Li(Text("aboba"))])])]))
    page2 = Page(Html([Head(Title(Text("aboba"))), Body([Ul([Img('src="http://i.imgur.com/pfp3T.jpg"')])])]))
    test(page1, page2)


def test_table():
    page1 = Page(Html([Head(Title(Text("aboba"))), Body([Table([Tr([Th(Text("aboba")), Th(Text("aboba"))])])])]))
    page2 = Page(Html([Head(Title(Text("aboba"))), Body([Table([Tr([Th(Text("aboba")), Td(Text("aboba"))])])])]))
    test(page1, page2)


if __name__ == '__main__':
    page = Page(Html([
        Head(Title(Text("aboba"))),
        Body(H1(Text("aboba")))
    ]))
    page.write_to_file("page.html")

    test_head_body()
    test_title()
    test_body()
    test_text()
    test_span()
    test_list()
    test_table()
