from django.urls import path
from . import views

# requête dossier views
urlpatterns = [
    path('', views.index, name='index'),
    path('sites/create/', views.siteCreate, name='formCreate'),
    path('sites/update/<int:site_id>/', views.siteUpdate, name='formEdit'),
    path('sites/delete/<int:site_id>/', views.siteDelete, name='siteDelete'),
    path('sites/<int:site_id>/', views.siteView, name='details'),
    
]