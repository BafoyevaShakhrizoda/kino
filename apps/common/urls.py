from django.urls import path

from apps.common.views import home,contact ,about


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]