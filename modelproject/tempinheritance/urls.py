from django.urls import path, re_path, include
from . import views

app_name = 'tempinheritance'

urlpatterns = [
    path('',views.tempinheritanceview,name='basehtml'),
    path('page1/', views.page1,name='page1'),
    path('page2/', views.page2,name='page2'),
    path('basehtml/', views.basehtml, name='basehtml')
]