
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm, UserForm, signupform 


from django.contrib.auth import authenticate,login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            user = authenticate (username = username,password=password)
            login(request,user)
            return redirect('/accounts/login')
        
    else:
        form = signupform()
        
    return render(request,'registration/signup.html',{'form':form})        

def profile(requset):
    profile = Profile.objects.get(user=requset.user)
    return redirect(reverse('dashboard:dashboard'),{'profile':profile})

def profile_edit(request):
    profiles = Profile.objects.get(user =request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profiles)
        if userform.is_valid() and profileform.is_valid() :
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('dashboard:dashboard'))
    
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profiles)
        
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})


def profile_user(requset):
    profile = Profile.objects.get(user=requset.user)
    return redirect(reverse('dashboard:dashboard'),{'profile':profile})

def profile_edit_user(request):
    profiles = Profile.objects.get(user =request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profiles)
        if userform.is_valid() and profileform.is_valid() :
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('dashboard:profile_user'))
    
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profiles)
        
    return render(request,'accounts/userprof.html',{'userform':userform,'profileform':profileform})

