from django.urls import path, re_path

from .views import (
	universe_view, 
	send_friend_request, 
	cancel_friend_request,
	accept_friend_request,
	delete_friend_request,
	universe_profile_view
)

app_name = 'universe'

urlpatterns = [
	path('', universe_view, name='universe'),
	re_path(r'^(?P<slug>[\w-]+)/$', universe_profile_view),
	re_path(r'^friend-request/send/(?P<id>[\w-]+)/$', send_friend_request),
	re_path(r'^friend-request/cancel/(?P<id>[\w-]+)/$', cancel_friend_request),
	re_path(r'^friend-request/accept/(?P<id>[\w-]+)/$', accept_friend_request),
	re_path(r'^friend-request/delete/(?P<id>[\w-]+)/$', delete_friend_request)
]