from django import forms
from .models import Post, Question, Answer
from django.utils import timezone


class FeedBackForm(forms.Form):
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if FeedBackForm.is_spam(self.cleaned_data):
            raise forms.ValidationError(u'Spam', code='spam')

    @staticmethod
    def is_spam(data):
        return True


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     if not is_ethic(message):
    #         raise forms.ValidationError(u'Not correct', code=12)
    #     return message + "\nThank you for your attention."

    def save(self):
        data = self.cleaned_data
        data['creation_date'] = timezone.now()
        post = Post(**data)
        post.save()
        return post


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def clean(self):
    #     return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        data['author_id'] = 1
        question = Question(**data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.IntegerField()

    def __init__(self, question_id=None, data=None):
        self._question_id = question_id
        if data is None:
            super(AnswerForm, self).__init__()
        else:
            super(AnswerForm, self).__init__(data)

    def clean(self):
        self.cleaned_data['question'] = self._question_id
        return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        text = data['text']
        author_id = 1
        question_id = self._question_id
        answer = Answer(text=text, author_id=author_id, question_id=question_id)
        answer.save()
        return answer
