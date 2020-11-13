from django.shortcuts import render
from .models import publications

def all_publications(request):
    pubs = Publication.objects.all()
    return render(request, "publications/all.html", {"publications": pubs})
