from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def recipe_list(request):
    return HttpResponse("I'm from django")
