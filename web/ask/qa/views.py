from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def all_posts(request):
    return render(request, '', )


def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'qa/post_details.html', {
        'post': post,
    })


def tag_details(request, id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, 'qa/tag_details.html', {
        'tag': tag,
    })


def all_tags(request):
    tags = Tag.objects.order_by('id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(tags, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'qa/all_tags.html', {
        'tags': page.object_list,
        'paginator': paginator,
        'page': page,
    })
