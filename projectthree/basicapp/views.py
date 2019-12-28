from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User
from basicapp.forms import UserForm,UserProfileInfo

#These lot of libraries will help us to login

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'index.html',context_dict)
@login_required
def user_logout(request):
    logout(request)
    return render(request,'index.html')
@login_required
def special():
    return HttpResponse("You are logged in nice")


def form_name_view(request):
    form=forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("TextArea: "+form.cleaned_data['text'])
    return render(request,'form_page.html',{'form':form})
def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'relative_url.html')

def base(request):
    return render(request,'base.html')
def register(request):

    registered=False
    user_form=UserForm()
    profile_form=UserProfileInfo()
    if request.method=="POST":

        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)


    return render(request,'Registration.html',{'userform':user_form,'profileform':profile_form,'registered':registered})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)                                #If user is active then redirect him to the home page
                return render(request,'index.html')

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("Invalid Detail supplied")

    else:
        return render(request,'Login.html',{})



# Create your views here.
