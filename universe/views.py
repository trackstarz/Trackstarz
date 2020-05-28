from django.conf import settings

from django.contrib import messages

from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404, reverse

from django.views.generic import ListView

from django.urls import reverse

import stripe

from userprofile.models import userprofile

from universe.models import friendrequest

from django.contrib.auth import get_user_model

from blog.forms import UserForm, BurstForm, CommentForm

from blog.models import Burst, Comment



# Create your views here.
User = get_user_model()


def universe_view(request):
	users = userprofile.objects.exclude(user=request.user)
	context = {
		'users': users
	}

	return render(request, "universe/universe.html", context)


def universe_profile_view(request, slug):
    if request.user.is_authenticated:
        a = request.user.userprofile
        links = a.friends.all().values_list('slug', flat=True)
    else:
        links = []
    
    p = userprofile.objects.filter(slug=slug).first()
    u = p.user
    cover = p.coverphoto
    picture = p.picture
    displayname = p.displayname
    username = u.username
    absolute_url = p.get_absolute_url
    sent_friend_requests = friendrequest.objects.filter(from_user=p.user)
    rec_friend_requests = friendrequest.objects.filter(to_user=p.user)

    friends = p.friends.all()

    button_status = 'none'
    if p not in request.user.userprofile.friends.all():
        button_status = 'not_friend'

        if len(friendrequest.objects.filter(from_user=request.user).filter(to_user=p.user)) == 1:
            button_status = 'friend_request_sent'

    

    entries = Burst.objects.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.save()
            myslug = '/universe/' + slug
            return redirect(myslug)
        else:
            print (comment_form.errors)
    
    else:
        comment_form = CommentForm()



    context = {
        'u': u,
        'button_status': button_status,
        'friends_list': friends,
        'sent_friend_requests': sent_friend_requests,
        'rec_friend_requests': rec_friend_requests,
        'burst': entries,
        'slug': slug,
        'link_list': links,
        'cover': cover,
        'picture': picture,
        'displayname': displayname,
        'username': username,
        'absolute_url': absolute_url,
        'comment_form' : comment_form
    }
    return render(request, "universe/universeprofile.html", context)



def send_friend_request(request, id):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest, created = friendrequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
		return HttpResponseRedirect('/universe')
		

def cancel_friend_request(request, id):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest = friendrequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
		frequest.delete()
		return HttpResponseRedirect('/universe')
		

def accept_friend_request(request, id):
	from_user = get_object_or_404(User, id=id)
	frequest = friendrequest.objects.filter(from_user=from_user, to_user=request.user).first()
	user1 = frequest.to_user
	user2 = from_user
	user1.userprofile.friends.add(user2.userprofile)
	user2.userprofile.friends.add(user1.userprofile)
	frequest.delete()
	return HttpResponseRedirect('/universe/{}'.format(request.user.userprofile.slug))


def delete_friend_request(request, id):
	from_user = get_object_or_404(User, id=id)
	frequest = friendrequest.objects.filter(from_user=from_user, to_user=request.user).first()
	frequest.delete()
	return HttpResponseRedirect('/universe/{}'.format(request.user.userprofile.slug))





