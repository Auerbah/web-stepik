Будем создавать сущности в базе данных, используя API django.models

1) Открываем интерпритатор python с загруженным окружением проекта
    $ python manage.py shell

2) Выполняем следующие команды:
    >>> from qa.models import Post
    >>> from django.utils import timezone
    >>> post = Post(title="new post 1", creation_date="1000-10-10")
    >>> post.save()
    >>> post = Post(title="new post 2", creation_date=timezone.now())
    >>> post.save()

3) Можно проверить в базе данных, что добавилось 2 строки:
    mysql> select * from blogposts;

4) Создадим новый объект в базе данных другим способом (за 1 строчку):
    >>> post = Post.objects.create(title="new post 2", creation_date=timezone.now())

5) Обновим объект:
    >>> post.title = "new post 3"
    >>> post.save()

6) Добавим еще одну модель:

    class Tag(models.Model):
        title = models.CharField(max_length=255)
        posts = models.ManyToManyField(Post)

        def __unicode__(self):
            return self.title

7) Накатим ее в базу данных:
    $ python manage.py makemigrations
    $ python manage.py migrate

8) В базе данных добавится 2 таблицы: qa_tag, qa_tag_posts
    mysql> show tables;

Посмотрим описание таблиц:
    mysql> describe qa_tag;
    mysql> describe qa_tag_posts;

В qa_tag будет всего 2 поля: id и title
В qa_tag_posts будет 3 поля: id, tag_id и post_id

9) Создадим объекты:
    >>> t = Tag(title="easy")
    >>> t.save()
    >>> p = Post(title="post 4", timezone.now())
    >>> p.save()

10) Проверим таблицы:
    mysql> select * from blogposts;
    mysql> select * from qa_tags;
    mysql> select * from qa_tags_posts;

В blogposts добавился новый объект, в qa_tags добавился новый объект, qa_tags_posts - пустая

11) Свяжем tag и post
    >>> t.posts.add(p)
    >>> t.save()

12) В таблицу qa_tag_posts добавилась 1 строка


