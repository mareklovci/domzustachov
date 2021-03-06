"""domzustachov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from markdownx import urls as markdownx
from django.conf import settings
from django.conf.urls.static import static

from .views import index
from django.contrib.flatpages import views


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # site
    url(r'^$', index, name='index'),
    url(r'^o-nas/$', views.flatpage, {'url': '/o-nas/'}, name='about'),

    # other
    url(r'^markdownx/', include(markdownx)),
    url(r'^photologue', include('photologue.urls', namespace='photologue')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
