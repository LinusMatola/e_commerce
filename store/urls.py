from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^1$',home),
    url(r'^cart/(?P<user_id>\d+)/$',cart_products),
    url(r'^product/(?P<p_id>\d+)/$',product_detail),
    url(r'^tocart/$',tocart,name='tocart'),
    url(r'^remove/$',remove,name='remove'),
]+ static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)