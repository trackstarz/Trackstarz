"""Trackstarz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import blog.views
import userprofile.views
from blog import views as blog_views
from django.conf import settings
from django.urls import include, path, re_path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bursts', blog_views.BurstView, 'burst')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', blog_views.home, name='home'),
	path('admin/doc/', include('django.contrib.admindocs.urls')),
   	path('register/', userprofile.views.register, name='register'),
	path('search/', userprofile.views.search, name='search'),
	path('login/', userprofile.views.user_login, name='login'),
    	path('paypal/',include('paypal.standard.ipn.urls')),
    	path('restricted/', userprofile.views.restricted, name='restricted'),
    	path('logout/', userprofile.views.user_logout, name='logout'),
	re_path(r'^cms/', include(wagtailadmin_urls)),
	re_path(r'^documents/', include(wagtaildocs_urls)),
	re_path(r'^pages/', include(wagtail_urls)),
	path('memberships/', include('memberships.urls', namespace='memberships')),
	path('universe/', include('universe.urls', namespace='universe')),
	path('api/', include(router.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

