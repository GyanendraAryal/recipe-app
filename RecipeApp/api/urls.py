from django.urls import path
from .views import *

urlpatterns = [
path("recipe/", recipe_list),
path("users/", users_list)
]
