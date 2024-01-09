from django.shortcuts import render
from .models import Site

# Create your views here.
def index(req):
    sites = Site.objects.all()
    return render(req, 'tp/index.html', {'sites': sites})