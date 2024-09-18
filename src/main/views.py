from django.http import HttpResponse
from django.shortcuts import render

def main_view(request):
    # return HttpResponse('<h1>Welcome to You Freeman</h1>')
    return render(request, "views/main.html", context={"name": "Dan Freeman"})
