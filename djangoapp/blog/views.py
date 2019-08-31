from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

@api_view(["GET"])
def hello_world(request):
    return Response({"message": "hello world"})