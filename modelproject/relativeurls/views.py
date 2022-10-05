from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'relativeurls/index.html')

def other(request):

    return render(request,'relativeurls/other.html')

def relative(request):

    return render(request,'relativeurls/relative_url_templates.html')