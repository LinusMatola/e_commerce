from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',home,name='store_home'),
    url(r'^cart/$',cart_products),
    url(r'^product/(?P<p_id>\d+)/$',product_detail),
    url(r'^tocart/',tocart,name='tocart'),
    url(r'^remove/$',remove,name='remove'),
]+ static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)