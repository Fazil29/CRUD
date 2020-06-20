from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show),
    path('entry', views.entry),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
]
