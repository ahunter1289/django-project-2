from django.shortcuts import render
from django.http import HttpResponse
from users.models import User

# Create your views here.

def users(request):
    users_list = User.objects.order_by('first_name')
    first_name_dict = {'firstnames':users_list}
    # my_dict = {'insert_me':'i a from the users.views.py'}
    return render(request,'users/index.html',context=first_name_dict)