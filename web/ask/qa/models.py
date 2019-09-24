from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=256)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return 'post/%d/' % self.pk

    class Meta:
        db_table = 'blogposts'
    #     ordering = ['-creation_date']
