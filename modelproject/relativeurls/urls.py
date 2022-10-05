from django.urls import path
from relativeurls import views

# template tagging
app_name = 'relativeurls'

urlpatterns = [
    path('',views.index),
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]