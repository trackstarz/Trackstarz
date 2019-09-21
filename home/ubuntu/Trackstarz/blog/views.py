from django.shortcuts import render, render_to_response, redirect, get_object_or_404

from django.template import RequestContext

from blog.models import Category, Burst, Comment, Reply, BurstLike, CommentLike, ReplyLike

from blog.forms import UserForm, BurstForm, CommentForm, ReplyForm, BurstLikeForm, CommentLikeForm, ReplyLikeForm

from django.http import HttpResponseRedirect, HttpResponse

from django.template import loader, Context

from django.contrib.auth import authenticate, login 

from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect

from django.utils import timezone

from userprofile.models import userprofile

from rest_framework import viewsets

from blog.serializers import CategorySerializer, BurstSerializer, CommentSerializer, ReplySerializer, BurstLikeSerializer, CommentLikeSerializer, ReplyLikeSerializer


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BurstView(viewsets.ModelViewSet):
    serializer_class = BurstSerializer
    queryset = Burst.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ReplyView(viewsets.ModelViewSet):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()


class BurstLikeView(viewsets.ModelViewSet):
    serializer_class = BurstLikeSerializer
    queryset = BurstLike.objects.all()


class CommentLikeView(viewsets.ModelViewSet):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()


class ReplyLikeView(viewsets.ModelViewSet):
    serializer_class = ReplyLikeSerializer
    queryset = ReplyLike.objects.all()





def home(request):
    context = RequestContext(request)
    entries = Burst.objects.all()[:100]
    
    global myburst
    global myid
    global is_liked
    
    



    if request.user.is_authenticated:
        p = request.user.userprofile
        friends = p.friends.all().values_list('slug', flat=True)
    else:
        friends = []
   

    if request.method == "POST":
        burst_form = BurstForm(request.POST or None) # Attempt to grab information from the raw form information.
        comment_form = CommentForm(request.POST or None)
        reply_form = ReplyForm(request.POST or None)
        burstlike_form = BurstLikeForm(request.POST or None)
        commentlike_form = CommentLikeForm(request.POST or None)
        replylike_form = ReplyLikeForm(request.POST or None)

        if burst_form.is_valid():
            burst = burst_form.save(commit=False)
            burst.author = request.user
            burst.timestamp = timezone.now()
            if 'picture' in request.FILES:
                burst.picture = request.FILES['picture']
            burst.save()

        else:
            print (burst_form.errors)


        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.save()
            return redirect("/")
        else:
            print (comment_form.errors)


        if reply_form.is_valid():
            reply_form.instance.user = request.user
            reply_form.save()
            return redirect("/")
        else:
            print (reply_form.errors)

        
        if burstlike_form.is_valid():
            burstlikes = BurstLike.objects.all()
            myburst = burstlike_form.save(commit=False)
            burstlike_form.instance.user = request.user

            if burstlikes.filter(burst=myburst.burst).exists() and burstlikes.filter(user=myburst.user).exists():
                burstlikes.filter(burst=myburst.burst, user=myburst.user).first().delete()
            else:
                burstlike_form.save()
                return redirect("/")
        else:
            print (burstlike_form.errors)


        if commentlike_form.is_valid():
            commentlikes = CommentLike.objects.all()
            mycomment = commentlike_form.save(commit=False)
            commentlike_form.instance.user = request.user

            if commentlikes.filter(comment=mycomment.comment).exists() and commentlikes.filter(user=mycomment.user).exists():
                commentlikes.filter(comment=mycomment.comment, user=mycomment.user).first().delete()
            else:
                commentlike_form.save()
                return redirect("/")
        else:
            print (commentlike_form.errors)



        if replylike_form.is_valid():
            replylikes = ReplyLike.objects.all()
            myreply = replylike_form.save(commit=False)
            replylike_form.instance.user = request.user

            if replylikes.filter(reply=myreply.reply).exists() and replylikes.filter(user=myreply.user).exists():
                replylikes.filter(reply=myreply.reply, user=myreply.user).first().delete()
            else:
                replylike_form.save()
                return redirect("/")
        else:
            print (replylike_form.errors)

        


    else:
        burst_form = BurstForm()
        comment_form = CommentForm()
        reply_form = ReplyForm()
        burstlike_form = BurstLikeForm()
        commentlike_form = CommentLikeForm()
        replylike_form = ReplyLikeForm()
        


    return render(request, 'blog/home.html', {'burst' : entries, 'burst_form' : burst_form, 'friends_list': friends, 'comment_form' : comment_form, 'reply_form' : reply_form, 'burstlike_form' : burstlike_form, 'commentlike_form' : commentlike_form, 'replylike_form' : replylike_form} )



def burst(request):
    # Like before, get the request's context.
    context = RequestContext(request)


    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        burst_form = BurstForm(data=request.POST) # Attempt to grab information from the raw form information.


        if user_form.is_valid() and burst_form.is_valid():
            user = user_form.save()
            burst = burst_form.save()
            burst.user = user
            #burst.bodytext = request.FILES['bodytext']
            burst.picture = request.FILES['picture']
            burst.save()

        else:
            print (user_form.errors, burst_form.errors)


    else:
        burst_form = BurstForm()
        user_form = UserForm()


    # Render the template depending on the context.
    return render(request, 'blog/home.html', {'user_form': user_form, 'burst_form' : burst_form})

