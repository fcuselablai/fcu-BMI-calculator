from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import BmiForm

def home(request):
    bmi = ''
    year = datetime.now().year
    form = BmiForm()
    if request.method=='POST':
        form = BmiForm(request.POST)
        if form.is_valid():
            form_cd = form.cleaned_data
            h = form_cd.get('height')
            w = form_cd.get('weight')
            bmi = round(w/(h**2),2)
            if bmi < 18.5:
                message = '過輕'
            elif bmi >= 18.5 and bmi < 24:
                message = '健康體位'
            elif bmi >= 24 and bmi < 27:
                message = '過重'
            elif bmi >= 27 and bmi < 30:
                message = '輕度肥胖'
            elif bmi >= 30 and bmi < 35:
                message = '中度肥胖'
            else:
                message = '重度肥胖'
    return render(request, 'index.html', locals())

