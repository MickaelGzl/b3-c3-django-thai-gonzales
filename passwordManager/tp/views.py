from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Site
from .forms import SiteForm

# Create your views here.
def index(req):
    sites = Site.objects.all()
    return render(req, 'tp/index.html', {'sites': sites})


def siteView(req, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(req, 'tp/details.html', {'site': site})


def siteCreate(req):
    if req.method == 'POST':
        form = SiteForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SiteForm()
    
    return render(req, 'tp/form.html', {'form': form})


def siteDelete(req, site_id):
    # Récupérer l'objet à supprimer
    site = get_object_or_404(site, pk=site_id)
    site.delete()
    return HttpResponseRedirect('/')
    
 