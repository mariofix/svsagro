from django.shortcuts import render, redirect
from core.utils import get_menus


def index(request):
    return redirect("step1")

def step1(request):
    context = {"modulos": get_menus()}
    return render(request, "optisort/step1.html", context)

def step2(request):
    context = {"modulos": get_menus()}
    return render(request, "optisort/step2.html", context)