from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Post, Tag


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def all_posts(request):
    return render(request, '', )


def post_details(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'qa/post_details.html', {
        'post': post,
    })


def tag_details(request, id):
    try:
        tag = Tag.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'qa/tag_details.html', {
        'tag': tag,
    })
