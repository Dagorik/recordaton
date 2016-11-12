"""recordaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^list/', login_required(NoteListView.as_view()), name="list-notes"),
    url(r'^create/', login_required(NoteCreateView.as_view()), name="create-note"),
    url(r'^detail/(?P<pk>[0-9]+)/', login_required(NoteDetailView.as_view()), name="detail-note"),
    url(r'^delete/(?P<pk>[0-9]+)/', login_required(NoteDeleteView.as_view()), name="delete-note"),
    url(r'^update/(?P<pk>[0-9]+)/', login_required(NoteUpdateView.as_view()), name="update-note"),
    
]
