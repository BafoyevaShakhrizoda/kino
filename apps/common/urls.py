# common/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='common-about'),
    path('', views.contact, name='common-contact'),
]