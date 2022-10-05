import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelproject.settings')

import django
django.setup()

import random
from home.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketplace','news','games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

         faketopic = add_topic()

         fakeurl = fakegen.url()
         fakename = fakegen.company()
         fakewebpage = Webpage.objects.get_or_create(topic=faketopic,url=fakeurl,name=fakename)[0]

         fakedate = fakegen.date()
         fakeaccessrecord = AccessRecord.objects.get_or_create(name=fakewebpage,date=fakedate)[0]


if __name__ == '__main__':
    print('pupulating script')
    populate(20)
    print("populating complete")