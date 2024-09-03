from django.shortcuts import render
from .forms import MyForm
import logging

logger = logging.getLogger('form_logger')

def ex02(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            logger.info(f'Form submitted: {form.cleaned_data}')
            return render(request, 'ex02/ex02.html', {'form': form, 'history': form.cleaned_data['text']})  
        
    form = MyForm()
    return render(request, 'ex02/ex02.html', {'form': form})
