from django.shortcuts import render
from django.http import HttpResponse
from .models import CPPCode
from datetime import date


# Create your views here.
def index(request):
    code = CPPCode.objects.all().order_by('-date')
    print(type(code))

    n = len(code)

    params = {'range': range(1, n), 'code': code}

    return render(request, "index.html", params)


def upload(request):
    if request.method == "POST":
        question = request.POST['question']
        code = request.POST['code']

        cppcode = CPPCode(question=question, code=code, date=date.today())
        cppcode.save()
    return render(request, "upload.html")
