from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create-page", views.createPage, name="create-page"),
    path('edit-page', views.editPage, name='edit-page'),
    path('save-edit-page', views.saveEdit, name='save-edit-page'),
    path('random-page', views.randomPage, name='random-page'),

    
]
