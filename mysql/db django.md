Настроим проект, чтобы посылать запросы к базе данных через python, используя окружение проекта
```python
'mysql': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'database_db',
    'USER': 'root',
    'PASSWORD': 'password',
    'HOST': '192.168.165.74',
    'PORT': '13306',
}
```
Нужно установить mysqlclient:
```
$ pip install mysqlclient
```
Запускаем проект:
```
$ python manage.py runserver
```
Если что-то не так введено, то будет выбрашено исключение

Запускаем shell:
```
$ python manage.py shell
```
Загружается django окружение и иможно выполнять команды на питоне

Выполняем запросы:
```python
>>> from django.db import connection, connections

# default_cur = connection.cursor()
# default_cur = connections['default'].cursor() аналогично первому

>>> cur = connections['mysql'].cursor()

>>> cur.execute("select * from user")

>>> for user in cur.fetchall(): # cur.fetchall() возвращает кортежи: ('alex', 'alex@gmail.com', None)
>>>     name, email, password = user
>>>     print(name)
```

Дальше будем использовать dajngo ORM для работы с базой данных

В models.py создадим новый класс:
```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return 'post/%d/' % self.pk

    class Meta:
        db_table = 'blogposts' # по умолчанию имя таблицы будет <app_name>_<class_name>
    #     ordering = ['-creation_date']
```
Создаем новую схему, которая потом будет накатываться в базу данных:
```    
$ python manage.py makemigrations
```
Чтобы увидеть схему, нужно выполнить:
```    
$ python manage.py sqlmigrate <app_name> <number>
```
Например:
```
$ python manage.py sqlmigrate polls 0001
```

Накатываем схему:
```
$ python manage.py migrate
```
Или
```
$ python manage.py migrate --database=mysql
```
Первая команда накатит в базу данных по умолчанию.

Нужно сделать mysql базу данных как default в settings.py 

Добавим несколько строк в БД через терминал (см как подключить через терминал в пред. статье)
```mysql
INSERT INTO blogposts VALUES (NULL, 'title', 'content1', '1000-10-01');
INSERT INTO blogposts VALUES (NULL, 'title', 'content1', '1000-10-01 23:59:59');
```
