from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def mainpage(request):
 return render(request, 'pages/mainpage.html')
def company(request):
 return render(request, 'pages/company_info.html')

def create(request):
 return render(request, 'pages/create.html')

def sign(request):
 return render(request, 'pages/sign.html')


def product(request):
 return render(request, 'pages/product.html')
