from django.shortcuts import render_to_response

from django.shortcuts import render

from django.template import RequestContext

from blog.models import Burst

from blog.forms import UserForm, BurstForm

from django.http import HttpResponseRedirect, HttpResponse

from django.template import loader, Context

from django.contrib.auth import authenticate, login 

from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect

from django.utils import timezone

from userprofile.models import userprofile




def home(request):
    context = RequestContext(request)
    entries = Burst.objects.all()[:100]
    if request.user.is_authenticated:
        p = request.user.userprofile
        friends = p.friends.all().values_list('slug', flat=True)
    else:
        friends = []
   

    if request.method == "POST":
        burst_form = BurstForm(data=request.POST) # Attempt to grab information from the raw form information.


        if burst_form.is_valid():
            burst = burst_form.save(commit=False)
            burst.author = request.user
            burst.timestamp = timezone.now()
            if 'picture' in request.FILES:
                burst.picture = request.FILES['picture']
            burst.save()

        else:
            print (burst_form.errors)


    else:
        burst_form = BurstForm()
        


    return render(request, 'blog/home.html', {'burst' : entries, 'burst_form' : burst_form, 'friends_list': friends} )



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

