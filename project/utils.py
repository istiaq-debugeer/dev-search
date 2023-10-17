from .models import Project,Profile,Tag
from users.models import Skill
from django.db.models import Q

def searchProjects(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
        print(search_query)
    skills=Skill.objects.filter(name__iexact = search_query)
    profile=Profile.objects.distinct().filter(Q(name__icontains=search_query) |Q(skill__in=skills))
    # profile = Profile.objects.all()

    return profile,search_query