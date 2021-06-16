from django.shortcuts import render

def ShowIndex(request):
    return render(request,"index.html")
