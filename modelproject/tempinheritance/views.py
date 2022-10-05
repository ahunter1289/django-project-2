from django.shortcuts import render

# Create your views here.

def tempinheritanceview(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'tempinheritance/index.html',context_dict)

def page1(request):

    return render(request,'tempinheritance/page1.html')

def page2(request):

    return render(request,'tempinheritance/page2.html')

def basehtml(request):

    return render(request,'tempinheritance/basehtml.html')