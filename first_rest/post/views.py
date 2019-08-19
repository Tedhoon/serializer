from .models import Post
from .serializer import PostSerializer

from rest_framework import viewsets


# 요 클래스가 api상의 CRUD를 담당(가능케 함)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer