class Elem:
    class Error(Exception):
        def __init__(self):
            self.msg = "Error: Elem"

    def __init__(self, tag: str, content=None, tag_type: str='double'):
        self.tag = tag
        self.content = []
        self.tag_type = tag_type
        if type(content) == list:
            self.content = content
        elif content is not None:
            self.content.append(content)

    def add_content(self, content):
        if type(content) is not Elem and type(content) is not str:
            raise Elem.Error
        if type(content) == list:
            self.content.extend(content)
        else:
            self.content.append(content)

    def __str__(self, lvl=0):
        tabulation = '  ' * lvl
        if self.tag_type == "simple":
            html =  '  ' * lvl + f"<{self.tag} "
            for i in self.content:
                html += str(i) + " "
            html += "/>"
            return html
        else:
            if len(self.content) == 0:
                return f"{tabulation}<{self.tag}></{self.tag}>"
            html = f"{tabulation}<{self.tag}>" + "\n"
            for i in self.content:
                if isinstance(i, Elem):
                    html += i.__str__(lvl + 1) + "\n"
                else:
                    html += '  ' * (lvl + 1) + str(i) + "\n"
            html += f"{tabulation}</{self.tag}>"
            return html


if __name__ == '__main__':
    html = Elem("html", content = [
                Elem("head", [Elem(
                    "title", content = '"Hello ground!"')]),
                Elem("body", [Elem(
                    "h1", content = '"Oh no, not again!"'),
                              Elem(
                    "img", content = 'src="http://i.imgur.com/pfp3T.jpg"', tag_type = "simple")])])

    # try:
    #     html.add_content(Elem("p", content = '"aboba"'))
    # except Elem.Error as e:
    #     print(e.msg)

    # try:
    #     html.add_content(1)
    # except Elem.Error as e:
    #     print(e.msg)

    print(html)
