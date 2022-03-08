from django.urls import path

from asuss import views

app_name='asuss'
urlpatterns=[
    path('home/',views.home)
]