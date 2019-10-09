from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Question


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
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 100
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(tags, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    paginator.baseurl = '?page='
    
    return render(request, 'qa/all_tags.html', {
        'tags': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def new_questions(request):
    tags = Question.objects.new()
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 10:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(tags, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    paginator.baseurl = '?page='

    return render(request, 'qa/new_questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'qa/question_details.html', {
        'question': question,
    })


def popular_questions(request):
    tags = Question.objects.popular()
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 10:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(tags, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    paginator.baseurl = '?page='

    return render(request, 'qa/popular_questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })
