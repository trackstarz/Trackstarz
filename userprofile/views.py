from django.shortcuts import render

from django.shortcuts import render_to_response

from userprofile.forms import UserForm, UserProfileForm

from blog.models import Burst

from userprofile.models import userprofile

from django.template import RequestContext

from django.contrib.auth import authenticate, login 

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from django.template import loader, Context

from django.views.decorators.csrf import csrf_protect

from django.db.models import Count, Q

from itertools import chain

from userprofile.serializers import userprofileSerializer

from rest_framework import viewsets




def search(request):
    queryset = Burst.objects.all() 
    
    query = request.GET.get('q')

    if query: 
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(bodytext__icontains=query) |
            Q(author__username__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query) |
            Q(author__email__icontains=query) |
            Q(categories__title__icontains=query) |
            Q(categories__description__icontains=query) |
            Q(comments__content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'query' : query
    }
    return render(request, 'userprofile/searchresults.html', context)





def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(
            request, 'userprofile/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
            
            
            
def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    serializer_class = userprofileSerializer

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Trackstarz account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'userprofile/user_login.html', {}, context)
        

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
    
    


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
    
    
    
def index(request):
    context = RequestContext(request)
    return render(request, 'blog/home.html', {}, context)
    
#def populateContext(request, context):
#	context['authenticated'] = request.user.is_authenticated()
#	if context['authenticated'] == True:
#		context['username'] = request.user.username
    
#def my_view(request):
 #   username = None
 #   if request.user.is_authenticated():
 #       username = request.user.username
        

