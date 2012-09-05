from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


from app.forms import RegistrationForm
from app.forms import PublishForm

from django.contrib.auth.models import User
from app.models import UserProfile
from app.models import Article 

def index(request):
    # If not logged in, then go to register page
    
    return render_to_response("home.html", {
        },
        context_instance = RequestContext(request)
    )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User.objects.create_user(email, #email is username
                                            email, #email
                                            password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            up = UserProfile(user=user)
            up.save()
            print user.first_name + user.last_name + " registered for the site."
            #request.session['next'] = '/'

            return authenticate(request, email, password)
    else:
        form = RegistrationForm()
    
    return render_to_response("login.html", {
            'form': form,
        },
        context_instance = RequestContext(request)
    )

def authenticate(request, email, password):
    user = auth.authenticate(username=email, password=password)
    if user is not None:
        if not user.is_active:
            auth.logout(request)
            return redirect('/') 

        auth.login(request, user)

        if 'next' in request.session:
            next = request.session['next']
            del request.session['next']
            return redirect(next)
        print user.first_name + user.last_name + " logged in."
        return redirect('/write') 
    else:
        form = RegistrationForm()
        return render_to_response("login.html", {
                'login_error': True, # indicates username / pword did not match
                'form': form,
            },
            context_instance = RequestContext(request)
        )

def publish(request):
    if not request.user.is_authenticated():
        print "User was not authenticated to write, redirected to registration."
        return register(request)
    if request.method == "POST":
        form = PublishForm(request.POST)
        if form.is_valid():
            formtitle = form.cleaned_data['title']
            formtext = form.cleaned_data['text']
            formuser = request.user
            print formtitle
            print formtext
            print formuser.first_name + formuser.last_name
            art = Article(title=formtitle, text=formtext, user=formuser)
            art.save()
            return redirect('/')
        else:
            print "SOMETHING IS WRONG"
            return redirect('/')
    else:
        form = PublishForm()

    return render_to_response("write.html", {
            'form': form
       },
       context_instance = RequestContext(request)
    )
        
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@csrf_protect
def login(request):
    if request.method == "POST":
        return authenticate(request, request.POST['email'], request.POST['password'])
    return redirect('/')

def userview(request, userid):
    print userid
    return redirect('/') 

def list(request, pagenumber):
    articles = Article.objects.all()
    print articles
    return render_to_response("list.html", {
        'articles': articles
        },
        context_instance = RequestContext(request)
    )


# Create your views here.
