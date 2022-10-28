from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework import status
from .models import Article





# Create your views here.
class ArticleView(APIView):
    def get(self, request, format=None):
        list=Article.objects.all()
        serializer= ArticleSerializer(list, many=True)
        print(list)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)