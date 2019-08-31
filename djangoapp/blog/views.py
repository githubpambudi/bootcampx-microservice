from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.serializers import CategorySerializer
from .models import Category


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "hello world"})


@api_view(["GET"])
def categories(request):
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True)
    return Response(serialized.data)


@api_view(["GET"])
def single_category(request, pk):
    queryset = Category.objects.get(pk=pk)
    serialized = CategorySerializer(queryset)
    return Response(serialized.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
