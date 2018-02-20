from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^invalid$',invalid,name='invalid'),
    url(r'^signup/$',signup,name='signup'),
    url(r'^logout/$',logout,name="logout"),
    url(r'^auth-check/$',auth_view,name='check'),
]