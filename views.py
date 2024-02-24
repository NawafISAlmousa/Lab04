from django.shortcuts import render
from django.http import HttpResponse

# Create our views here
TAX = 0.15

def index(request):
    return HttpResponse("This is a site to calculate tax")

def taxCalc(request, number):
    return HttpResponse(f"The number after tax is {number+(number*TAX)}.")

def taxrate(request):
    return render(request, "Taxes/index.html", {
        "tax": TAX*100
    })