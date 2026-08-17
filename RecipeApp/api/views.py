from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.
@api_view(["GET"])
def recipe_list(request):
    return Response("I'm from django")


@api_view(["GET"])
def users_list (request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
