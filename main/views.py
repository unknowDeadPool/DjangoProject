from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer

@api_view(["GET", "POST"])
def categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    else:
        return Response({"message":"Hello Makers"})

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
