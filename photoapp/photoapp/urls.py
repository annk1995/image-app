
from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^photos/',include('photos.urls')),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage)
]
