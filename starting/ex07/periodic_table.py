import sys

def read_elements():
    f = open('periodic_table.txt', 'r')
    elements = {}
    for line in f:
        line = line.strip()
        if line:
            key, value = line.split(" = ")
            elements[key] = value
    f.close()
    return elements


if __name__ == '__main__':
    HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Periodic Table</title>
  <style>
    table{{
      border-collapse: collapse;
    }}
    h4 {{
      text-align: center;
    }}
    ul {{
      list-style:none;
      padding-left:0px;
    }}
  </style>
</head>
<body>
  <table>
    {body}
  </table>
</body>
</html>
    """

    TEMPLATE = """
    <td style="border: 3px solid red; padding:5px">
        <h4>{name}</h4>
        <ul>
          <li>{number}</li>
          <li>{small}</li>
          <li>{molar}</li>
          <li style="width:175px;">{electron}</li>
        </ul>
    </td>
    """

    TEMPLATE_EMPTY = """
    <td></td>
    """

    elements = read_elements()

    body = ""
    pos = 0
    for key, value in elements.items():
        name = key
        position, number, small, molar, electron = value.split(", ")
        position = int(position.split(":")[1])
        if position == 0:
            body += "<tr>"
            body += TEMPLATE.format(name=name, number=number, small=small, molar=molar, electron=electron)
        else:
            if pos == 0:
                tmp = pos
                while tmp < position - 1:
                    body += TEMPLATE_EMPTY
                    tmp += 1
            if (pos == 1 or pos == 2) and position == 12:
                tmp = 1
                while tmp < position - 1:
                    body += TEMPLATE_EMPTY
                    tmp += 1
            if (pos == 5 or pos == 6) and position == 3:
                tmp = 1
                while tmp < position - 1:
                    body += TEMPLATE_EMPTY
                    tmp += 1
                    
            body += TEMPLATE.format(name=name, number=number, small=small, molar=molar, electron=electron)
            if position == 17:
                body += "</tr>"
                pos += 1
        
    f = open('periodic_table.html', 'w')
    f.write(HTML.format(body=body))
    f.close()
