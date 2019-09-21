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
import universe.views
import memberships.views
from blog import views as blog_views
from django.conf import settings
from django.urls import include, path, re_path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', blog_views.CategoryView, 'category')
router.register(r'bursts', blog_views.BurstView, 'burst')
router.register(r'comments', blog_views.CommentView, 'comment')
router.register(r'replies', blog_views.ReplyView, 'reply')
router.register(r'burstlikes', blog_views.BurstLikeView, 'burstlike')
router.register(r'commentlikes', blog_views.CommentLikeView, 'commentlike')
router.register(r'replylikes', blog_views.ReplyLikeView, 'replylike')
router.register(r'userprofiles', userprofile.views.UserprofileView, 'userprofile')
router.register(r'friendrequests', universe.views.FriendrequestView, 'friendrequest')
router.register(r'memberships', memberships.views.MembershipView, 'membership')
router.register(r'usermemberships', memberships.views.UserMembershipView, 'usermembership')
router.register(r'subscriptions', memberships.views.SubscriptionView, 'subscription')


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
	path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

