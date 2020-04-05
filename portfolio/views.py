from django.shortcuts import render
from .models import Project
from gallery.models import Picture


def home(request):
    projects = Project.objects.all()
    pictures = Picture.objects.all()

    mydict = {'projects':projects, 'pictures':pictures}
    return render(request, 'portfolio/home.html', context=mydict)
