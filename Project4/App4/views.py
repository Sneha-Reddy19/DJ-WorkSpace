from django.shortcuts import render

def ShowIndex(request):
    return render(request,"main.html")
