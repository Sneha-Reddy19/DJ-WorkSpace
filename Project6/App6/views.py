from django.shortcuts import render

def ShowIndex(request):
    emp_info = {"idno":101,"name":"Ravi","salary":185000.00}
    return render(request,"six.html",emp_info)

