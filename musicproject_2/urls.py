"""musicproject_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from userapp.views import indexpage
from django.conf import settings
# from album_app.views import AlbumViewSet

from rest_framework import routers
from django.conf.urls.static import static

# router = routers.DefaultRouter()
# router.register('albums', AlbumViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', indexpage),
    path('', include('userapp.urls')),
    path('', include('song_app.urls')),
    path('', include('artist_app.urls')),
    path('', include('album_app.urls')),
    # path('', include("rest_framework.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
