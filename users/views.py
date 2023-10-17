from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Skill
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from users.forms import ProfileForm,UserCreateForm,SkillForm
from project.utils import searchProjects
# Create your views here.

class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/users')
        return render(request,'users/login.html')

    def post(self,request):

        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            try:
                user=User.objects.get(username=username)
            except:
                print("username is not there")

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/users')
            else:
                print("username or password are incorrect")
        return render(request,'users/login.html')
def Logout(reqeust):
    logout(reqeust)
    return render(reqeust,'users/login.html')
def profiles(request):
    profile,search_query=searchProjects(request)

    context={
        "profile":profile,
        "search_query":search_query
    }
    return render(request,'users/profiles.html',context=context)

def UserProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    topSkills=profile.skill_set.exclude(description__exact="")
    otherskill=profile.skill_set.filter(description="")
    context={
        "profile":profile,
        "topskill":topSkills,
        "otherskill":otherskill
    }
    return render(request,'users/user-profile.html',context=context)

@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    skills=profile.skill_set.all()
    project=profile.project_set.all()


    context={
        'profile':profile,
        'skills':skills,
        'project':project
    }
    return render(request,'users/account.html',context=context)
def registerUser(request):


    page='register'
    form=UserCreateForm
    if request.method=="POST":
        form=UserCreateForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'register successfully')
            return redirect('/users/login')
        messages.error(request,'password or username wrong')
    context={
        'page':page,
        'form':form
    }
    return render(request,'users/login.html',context=context)
@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/users/account')
    context={'form':form}
    return render(request,'users/profile_form.html',context=context)
login_required(login_url='login')
def createSkill(request):
    profile=request.user.profile
    form=SkillForm()
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=profile
            skill.save()
            messages.success(request,'succesfully added')
            return redirect('/users/account')
        messages.error(request,'there is an error occured')
    context={
        'form':form

    }
    return render(request,'users/create_skill.html',context=context)

def UpdateSkill(request,pk):
    page='update'
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    form=SkillForm(instance=skill)
    if request.method=='POST':
        form=SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'succesfully edited')
            return redirect('/users/account')
        messages.error(request,'there is an error occured')
    context={
        'form':form,
        'page':page

    }
    return render(request,'users/create_skill.html',context=context)

def deleteskill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    if request.method=='POST':
        skill.delete()
        return redirect('/users/account')
    context={'object':skill}
    return render(request,'delete_template.html',context)