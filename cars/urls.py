from django.urls import path
from .views import *


urlpatterns = [
    path('home/', hello_world),
    path('allcars/', carview),
    path('filterblackcars/', filterview),
    path('deletecar/', deleteview),
    path('insertcar/', createview)
]

