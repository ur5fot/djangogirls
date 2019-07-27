from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

from .serializers import PostSerializer


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(post_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        post = get_object_or_404(Post.objects.all(), pk=pk)
        post.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)
