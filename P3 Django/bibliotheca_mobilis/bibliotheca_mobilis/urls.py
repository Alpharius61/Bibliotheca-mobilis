"""bibliotheca_mobilis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from registration import views as r_views
from community import views as com_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accountCreation/', r_views.accountCreation, name='accountCreation'),
    path('connection/', r_views.connection, name='connection'),
    path('logout/', r_views.logOut, name='logout'),
    path('characterCreation/', com_views.characterCreationView,name='characterCreation'),
    path('ajax/load-races/', com_views.load_races, name='ajaxLoadRaces'),
    path('character/<str:name>', com_views.characterView, name='characterView'),
    path('charactersList/', com_views.charactersList, name='charactersList'),
    path('armyCreation/', com_views.armyCreationView,name='armyCreation'),
    path('army/<str:name>', com_views.armyView, name='armyView'),
    path('armiesList/', com_views.armiesList, name='armiesList'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)