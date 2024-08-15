from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brazil/", views.brazil, name="brazil"),
    path("eua/", views.eua, name="eua"),

]