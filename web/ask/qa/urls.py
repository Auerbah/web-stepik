from django.urls import path

from . import views

app_name = 'qa'

urlpatterns = [
    path('', views.test, name='index'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:id>/', views.test, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new'),
    path('post/<int:id>', views.post_details, name='post-details'),
    path('tag/<int:id>', views.tag_details, name='tag-details'),
]
