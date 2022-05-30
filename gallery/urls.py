from django.conf import settings
from django.urls import re_path as url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url ('^$', views.index, name='index'),
    url('^image/(?P<category_name>\w+)/(?P<image_id>\d+)', views.single, name='single'),
    url('^location/(?P<image_location>\w+)', views.location_filter, name = 'location_filter'),
    url('^search/', views.search_image, name='search_image')
]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)