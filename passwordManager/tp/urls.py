from django.urls import path
from . import views

# requête dossier views
urlpatterns = [
    path('', views.index, name='index'),
    path('sites/create/', views.siteCreate, name='formCreate'),
    path('sites/<int:site_id>/', views.siteView, name='details'),
    path('sites/delete/', views.siteView, name='siteDelete'),
    
]