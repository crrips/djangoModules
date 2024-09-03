from django.shortcuts import render

def interpolate_color(start_color, end_color, factor):
    return tuple(
        int(start_color[i] + (end_color[i] - start_color[i]) * factor)
        for i in range(3)
    )

def ex03(request):
    
    white = (255, 255, 255)
    noir = (0, 0, 0)
    rouge = (255, 0, 0)
    bleu = (0, 0, 255)
    vert = (0, 128, 0)
    
    n_shades = 51
    
    shades = {
        "noir": [],
        "rouge": [],
        "bleu": [],
        "vert": []
    }
    
    for i in range(n_shades):
        factor = i / (n_shades - 1)
        shade = interpolate_color(white, noir, factor)
        shades["noir"].append(shade)
        shade = interpolate_color(white, rouge, factor)
        shades["rouge"].append(shade)
        shade = interpolate_color(white, bleu, factor)
        shades["bleu"].append(shade)
        shade = interpolate_color(white, vert, factor)
        shades["vert"].append(shade)

    table_rows = ''
    for i in range(51):
        table_rows += '<tr>'
        table_rows += f'<td style="background-color:rgb{shades["noir"][i]}"></td>'
        table_rows += f'<td style="background-color:rgb{shades["rouge"][i]}"></td>'
        table_rows += f'<td style="background-color:rgb{shades["bleu"][i]}"></td>'
        table_rows += f'<td style="background-color:rgb{shades["vert"][i]}"></td>'
        table_rows += '</tr>'
    
    context = {
        "table_rows": table_rows
    }
    
    return render(request, 'ex03/ex03.html', context)
