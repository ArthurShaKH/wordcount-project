from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name = 'homePage'),
    url(r'^countedWords/', views.count, name='count'),
    url(r'^about/', views.about, name='about'),
]
