from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import *
from .forms import *
from .models import *
import urllib
from django.conf import settings
import json
from django.contrib import messages

# Create your views here.
def login(request):
    if 'next' in request.GET:
        next_page = request.GET['next']
        return render(request,'login.html', {'next_page': next_page})
    else:
        return render(request, 'login.html')

def index(request):
    return redirect('store:store_home')
def invalid(request):
    error = "a"
    return render(request, 'login.html', {'error': error})

def home(request):
    if request.user.is_authenticated():
        return index(request)
        #return HttpResponse("hmmm")
    else:
        return login(request)

def signup(request):
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            img = request.FILES['profile_pic']
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']


            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            print(result)
            ''' End reCAPTCHA validation '''

            if result['success']:
                a = User.objects.create_user(username=username,password=password,email=email)
                a
                obj = userinfo(user=a,firstname=firstname,lastname=lastname,profile_pic=img)
                obj.save()
                return redirect('login:home')
            else:
                #messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                err = "Invalid Captcha"
                return render(request, 'register.html', {'err': err})
        else:
            err = form.errors
            return render(request, 'register.html', {'err': err})
    else:
        form=regform()
        return render(request,'register.html')
#    return render(request, 'register.html')

def auth_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        if 'next' in request.POST:
            nextp = request.POST['next']
            auth.login(request,user)
            return redirect(nextp)
        else:
            auth.login(request, user)
            return index(request)
    else:
        return redirect('login:invalid')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')