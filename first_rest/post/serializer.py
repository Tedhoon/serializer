from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        fields = ('id','title','body')   #웬만하면 튜플로 씁시다! 
 
        read_only_fields = ('title',)
        # write_only_fields