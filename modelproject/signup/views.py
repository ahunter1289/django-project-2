from django import forms
from django.shortcuts import render
from . import forms
from signup.forms import NewUserForm

# Create your views here.

def signup_form_view(request):

    form = forms.SignupForm()

    return render(request,'signup/form.html',{'form':form})

def index(request):
    return render(request,'signup/index.html')

def email(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error Form Invalid")

    return render(request,'signup/form.html',{'form':form})