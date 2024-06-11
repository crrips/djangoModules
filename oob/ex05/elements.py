from elem import Elem

class Html(Elem):
    def __init__(self, content=None):
        super().__init__("html", content=content)


class Head(Elem):
    def __init__(self, content=None):
        super().__init__("head", content=content)


class Body(Elem):
    def __init__(self, content=None):
        super().__init__("body", content=content)


class Title(Elem):
    def __init__(self, content=None):
        super().__init__("title", content=content)


class Meta(Elem):
    def __init__(self, content=None):
        super().__init__("meta", content=content, tag_type="simple")


class Img(Elem):
    def __init__(self, content=None):
        super().__init__("img", content=content, tag_type="simple")


class Table(Elem):
    def __init__(self, content=None):
        super().__init__("table", content=content)


class Th(Elem):
    def __init__(self, content=None):
        super().__init__("th", content=content)


class Tr(Elem):
    def __init__(self, content=None):
        super().__init__("tr", content=content)


class Td(Elem):
    def __init__(self, content=None):
        super().__init__("td", content=content)


class Ul(Elem):
    def __init__(self, content=None):
        super().__init__("ul", content=content)


class Ol(Elem):
    def __init__(self, content=None):
        super().__init__("ol", content=content)


class Li(Elem):
    def __init__(self, content=None):
        super().__init__("li", content=content)


class H1(Elem):
    def __init__(self, content=None):
        super().__init__("h1", content=content)


class H2(Elem):
    def __init__(self, content=None):
        super().__init__("h2", content=content)


class P(Elem):
    def __init__(self, content=None):
        super().__init__("p", content=content)


class Div(Elem):
    def __init__(self, content=None):
        super().__init__("div", content=content)


class Span(Elem):
    def __init__(self, content=None):
        super().__init__("span", content=content)


class Hr(Elem):
    def __init__(self, content=None):
        super().__init__("hr", content=content, tag_type="simple")


class Br(Elem):
    def __init__(self, content=None):
        super().__init__("br", content=content, tag_type="simple")


if __name__ == '__main__':
    print(Html(
        [Head(
            Title('"Hello ground!"')), 
        Body([
            H1('"Oh no, not again!"'), 
            Img('src="http://i.imgur.com/pfp3T.jpg"')])]))
            