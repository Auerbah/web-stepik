from django.urls import path

from . import views

app_name = 'qa'

urlpatterns = [
    # path('', views.test, name='index'),
    path('', views.new_questions, name='new-questions'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:id>/', views.question_details, name='question-details'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.popular_questions, name='popular-questions'),
    path('new/', views.test, name='new'),

    path('post/<int:id>', views.post_details, name='post-details'),
    path('tag/<int:id>', views.tag_details, name='tag-details'),
    path('all_tags/', views.all_tags, name='all-tags'),
]
