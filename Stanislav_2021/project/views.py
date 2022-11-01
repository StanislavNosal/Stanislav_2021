from django.shortcuts import render
from .models import Project

def project_index(request):
    projects = Project.objects.all()
    context={
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(recuest, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'projects': project
    }
    return render(recuest, 'project_detail.html', context)
