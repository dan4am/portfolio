from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    login_form = AuthenticationForm()
    return render(request=request, template_name="views/login.html", context={'login_form': login_form})
