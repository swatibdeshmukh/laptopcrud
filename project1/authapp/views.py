from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from random import randint
from django.conf import settings
from django.core.mail import send_mail
#from django.http import HttpResponse

# Create your views here.
otp = randint(1000, 9999)
def Register_View(request):
    form = UserCreationForm()
    template_name = 'authapp/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request, template_name, context)
def login_View(request):
    template_name = 'authapp/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')
        global new
        user = authenticate(username=un, password=pw)
        new = user
        if user is not None:
            email = request.POST.get('e')
            subject = 'welcome to gfg world'
            message = f'Hi {user.username}, thank you for registering in python webdevelopment world ..your otp is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, 'swatideshmukh731@gmail.com']
            send_mail( subject, message, email_from, recipient_list )

            #login(request, user)#session create
            return redirect('otp_url')
    return render(request, template_name, context)
def Logout_View(request):
    logout(request)
    return redirect('login_url')

def mail_View(request):
   
    if request.method=="post":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        login(request,user)
        subject = 'welcome to gfg world'
        message = f'Hi {user.username}, thank you for registering in webworld.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail( subject, message, email_from, recipient_list )
       
        return HttpResponse('<h1>email sent</h1>')
    template_name='authapp/signupformail.html'
    context={}
    return render(request, template_name, context)

def OTPView(request):
    template_name = 'authapp/otp.html'
    context = {}
    if request.method == 'POST':
        otp1 = int(request.POST.get('otp'))
        if otp == otp1:
            login(request, new)
            return redirect('showlaptop_url')
    return render(request, template_name, context) 