from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProjectForm
from .models import Project,Tag
from django.core.paginator import  Paginator,PageNotAnInteger,EmptyPage


def home(request):
    return render(request,'index.html')

def projects(request):
    project=Project.objects.all()
    page=request.GET.get('page')
    results=3
    paginator=Paginator(project,results)
    try:
        project=paginator.page(page)
    except PageNotAnInteger:
        page= 1
        project=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
    context={
        "project":project
    }
    return render(request,'projects/projects.html',context=context)

def project(request,pk):
    project=Project.objects.filter(id=pk)
    context={
        "project":project
    }

    return render(request,'projects/singleproject.html',context=context)

def createProject(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method=="POST":
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            form.save()
            return redirect('/users/account')
    context={
        "form":form
    }
    return render(request, 'projects/projectform.html',context=context)
def UpdateProject(request, pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=="POST":
        form=ProjectForm(request.POST,instance=project )
        if form.is_valid():
            form.save()
        return redirect('/users/account')

    context={
        "form":form
    }
    return render(request, 'projects/projectform.html',context=context)
def DeleteProject(request,pk):
    profile=request.user.profile
    try:
        project=profile.project_set.get(id=pk)
        project.delete()
    except:
        return HttpResponse('no item is available for remove')

    context={'object':project}

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))