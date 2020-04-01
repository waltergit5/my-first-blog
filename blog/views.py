from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post  # the dot in .models suggests modules is in current directory
                           # without .py
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
'''Render has two functions.Request to take user input from the internet and giving the template file blog/post_list.htm
{} some things for the template to use (i.e) posts'''

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})