import json

from django.shortcuts import HttpResponse, redirect


class HttpResponseAjax(HttpResponse):
    def __init__(self, status='ok', **kwargs):
        kwargs['status'] = status
        super(HttpResponseAjax, self).__init__(
            content=json.dumps(kwargs),
            content_type='application/json',
        )


class HttpResponseAjaxError(HttpResponseAjax):
    def __init__(self, code, message):
        super(HttpResponseAjaxError, self).__init__(
            status='error', code=code, message=message
        )


def login_required_ajax(view):
    def view2(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        elif request.is_ajax():
            return HttpResponseAjaxError(
                code='no_auth', message='Требуется авторизация'
            )
        else:
            redirect('login/?continue=' + request.get_full_path())
    return view2


# @login_required_ajax
# def comment_add(request):
#     form = AddCommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save()
#         return HttpResponseAjax(comment_id=comment.id)
#     else:
#         return HttpResponseAjaxError(code='bad_params', message=form.errors.as_text())
#         # return HttpResponseAjaxError(code='bad_params', message=form.errors.as_json())
