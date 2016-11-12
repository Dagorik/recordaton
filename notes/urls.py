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

urlpatterns = [
	url(r'^list/', NoteListView.as_view(), name="list-notes"),
    url(r'^create/', NoteCreateView.as_view(), name="create-note"),
    url(r'^detail/(?P<pk>[0-9]+)/', NoteDetailView.as_view(), name="detail-note"),
    url(r'^delete/(?P<pk>[0-9]+)/', NoteDeleteView.as_view(), name="delete-note"),
    url(r'^update/(?P<pk>[0-9]+)/', NoteUpdateView.as_view(), name="update-note"),
]
