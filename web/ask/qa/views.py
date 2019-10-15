from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import FeedBackForm, AddPostForm, AskForm, AnswerForm
from .models import Post, Tag, Question


def test(request, *args, **kwargs):
    try:
        print(request.GET.get('id'))
    except:
        pass
    return HttpResponse('OK')


def redirect(request):
    return HttpResponseRedirect('/redirected/')


def redirected(request):
    # return HttpResponseRedirect('/r/')
    return render(request, 'qa/redirected.html')


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

    if request.method == "POST":
        print(request.POST)
        form = AnswerForm(question.id, request.POST)
        if form.is_valid():
            print("saved")
            form.save()
            return HttpResponseRedirect(question.get_url())
        print("not valid")
        return render(request, 'qa/question_details.html', {
            'question': question,
            'form': form
        })
    else:

        form = AnswerForm(question.id)
        return render(request, 'qa/question_details.html', {
            'question': question,
            'form': form
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


def feedback(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            HttpResponseRedirect('/feedback/')
    else:
        form = FeedBackForm()
    return render(request, 'qa/feedback.html', {'form': form})


@csrf_exempt
def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)

    else:
        form = AddPostForm()
    return render(request, 'qa/add_post.html', {'form': form})


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)

    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})
