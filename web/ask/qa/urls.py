from django.urls import path

from . import views

app_name = 'qa'

urlpatterns = [
    # path('', views.test, name='index'),
    path('', views.new_questions, name='new-questions'),
    path('r/', views.redirect, name='redirect'),
    path('redirected/', views.redirected, name='redirected'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:id>/', views.question_details, name='question-details'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular_questions, name='popular-questions'),
    path('new/', views.test, name='new'),
    path('post/<int:id>', views.post_details, name='post-details'),
    path('post/add/', views.add_post, name='add-post'),
    path('tag/<int:id>', views.tag_details, name='tag-details'),
    path('all_tags/', views.all_tags, name='all-tags'),
    path('feedback/', views.feedback, name='feedback'),
    path('test/', views.test, name='test'),
    path('cookies/', views.cookies, name='cookies'),
]
