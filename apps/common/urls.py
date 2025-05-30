from django.urls import path

from apps.common.views import index,contact ,about


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]