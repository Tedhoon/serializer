from .models import Post
from rest_framework import serializers

class PostSerializer(serializer.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        fields = ['title','body']