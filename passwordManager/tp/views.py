from django.shortcuts import render, get_object_or_404
from .models import Site

# Create your views here.
def index(req):
    sites = Site.objects.all()
    return render(req, 'tp/index.html', {'sites': sites})


def siteView(req, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(req, 'tp/details.html', {'site': site})