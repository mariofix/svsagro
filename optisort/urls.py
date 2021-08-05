
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("step1/", views.step1, name="step1"),
    path("step2/", views.step2, name="step2"),
]
