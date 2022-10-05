import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelproject.settings')

import django
django.setup()

import random
from users.models import User
from faker import Faker

fakegen = Faker()

def populate(N=20):

    for entry in range(N):

         firstname = fakegen.first_name()
         lastname = fakegen.last_name()

         fakeuser = User.objects.get_or_create(first_name=firstname,last_name=lastname)

if __name__ == '__main__':
    print('pupulating script')
    populate(20)
    print("populating complete")