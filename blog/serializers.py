from rest_framework import serializers

from blog.models import Post

from rest_framework.serializers import ModelSerializer

#
# class PostSerializer(ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         fields = (
#              'title', 'text', 'created_date', 'published_date', 'author_id', 'author'
#         )




class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    text = serializers.CharField()
    created_date = serializers.CharField()
    published_date = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()
        return instance

