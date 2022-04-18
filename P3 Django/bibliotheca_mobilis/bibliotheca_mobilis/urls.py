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
from bibliotheca import views as bibli_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # User
    path('accountCreation/', r_views.accountCreation, name='accountCreation'),
    path('connection/', r_views.connection, name='connection'),
    path('logout/', r_views.logOut, name='logout'),

    # Creation content
    path('ajax/load-races/', com_views.load_races, name='ajaxLoadRaces'),
    path('characterCreation/', com_views.characterCreationView,name='characterCreation'),
    path('armyCreation/', com_views.armyCreationView,name='armyCreation'),
   
    # Creation view (list and element)
    path('charactersList/', com_views.charactersList, name='charactersList'),
    path('character/<str:name>', com_views.characterView, name='characterView'),
    path('character/update/<int:id>', com_views.characterUpdate, name='characterUpdate'),
    path('armiesList/', com_views.armiesList, name='armiesList'),
    path('army/<str:name>', com_views.armyView, name='armyView'),

    # Bibliotheca view

    path('bibliotheca/tree/', bibli_views.showTree, name='tree'),
    path('bibliotheca/tree/articles/<str:name>', bibli_views.bibliothecaArticle, name='univers'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)