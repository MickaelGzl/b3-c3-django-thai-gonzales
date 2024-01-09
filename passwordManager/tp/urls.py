from django.urls import path
from . import views

# requête dossier views
urlpatterns = [
    path('', views.index, name='index'),
    path('sites/<int:site_id>/', views.siteView, name='details'),
]