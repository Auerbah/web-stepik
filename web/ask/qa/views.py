from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import FeedBackForm, AddPostForm, AskForm, AnswerForm, SignupForm, LoginForm
from .models import Post, Tag, Question


def test(request, *args, **kwargs):
    try:
        print(request.GET.get('id'))
    except:
        pass
    return HttpResponse('OK')


def cookies(request):
    print(request.COOKIES)
    resp = HttpResponse('OK')
    # resp.set_cookie('sessid', '3', expires=(datetime.now() - timedelta(hours=3) + timedelta(seconds=30)))
    return resp


def redirect_view(request):
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


# @login_required
def question_details(request, id):
    question = get_object_or_404(Question, id=id)

    if request.user.is_authenticated and request.method == "POST":
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


# @login_required(login_url='/login/')
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if request.user.is_authenticated and form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        form = SignupForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return HttpResponseServerError()
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})


def login_view(request):
    url = request.GET.get('next', '/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(url)
            else:
                form.add_error(None, 'Username does not exist or password is not correct')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {'form': form})
