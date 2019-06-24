from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'signup', views.signup),
    url(r'logout', views.logout),



]