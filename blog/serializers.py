from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ('title', 'text', 'created_date', 'published_date', 'author_id')
