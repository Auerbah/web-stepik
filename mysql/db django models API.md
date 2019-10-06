Будем создавать сущности в базе данных, используя **API django.models**

Открываем интерпритатор python с загруженным окружением проекта:
```
$ python manage.py shell
```
Выполняем следующие команды:
```
>>> from qa.models import Post
>>> from django.utils import timezone
>>> post = Post(title="new post 1", creation_date="1000-10-10")
>>> post.save()
>>> post = Post(title="new post 2", creation_date=timezone.now())
>>> post.save()
```
Можно проверить в базе данных, что добавилось 2 строки:
```
mysql> select * from blogposts;
```
Создадим новый объект в базе данных другим способом (за 1 строчку):
```
post = Post.objects.create(title="new post 2", creation_date=timezone.now())
```
Обновим объект:
```
>>> post.title = "new post 3"
>>> post.save()
```
Добавим еще одну модель:
```
class Tag(models.Model):
    title = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return self.title
```
Накатим ее в базу данных:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
В базе данных добавится 2 таблицы: **qa_tag**, **qa_tag_posts**
```
mysql> show tables;
```
Посмотрим описание таблиц:
```
mysql> describe qa_tag;
mysql> describe qa_tag_posts;
```
В qa_tag будет всего 2 поля: **id** и **title**\
В qa_tag_posts будет 3 поля: **id**, **tag_id** и **post_id**\
Создадим объекты:
```
>>> t = Tag(title="easy")
>>> t.save()
>>> p = Post(title="post 4", timezone.now())
>>> p.save()
```
Проверим таблицы:
```
mysql> select * from blogposts;
mysql> select * from qa_tags;
mysql> select * from qa_tags_posts;
```
В blogposts добавился новый объект, в **qa_tags** добавился новый объект, **qa_tags_posts** - пустая\
Свяжем **tag** и **post**
```
>>> t.posts.add(p)
>>> t.save()
```
В таблицу **qa_tag_posts** добавилась 1 строка


