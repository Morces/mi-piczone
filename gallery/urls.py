from django.urls import re_path as url
from . import views


urlpatterns = [
    url (r'^$', views.index, name='index'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)', views.single, name='single')
]