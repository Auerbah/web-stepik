# web-stepik

#### Подготовка
Клонируем репозиторий
```
git clone https://github.com/Auerbah/web-stepik
mv web-stepik/web ~/
```
Устанавливаем django нужной версии, иначе проект не будет запускаться
```
sudo pip3 install Django==2.0
```
Проверяем, что всё установилось
```
pip3 list
```
Возможно процесс не будет завершаться, тогда нужно прервать процесс и проверить установился ли django версии 2.0,
если нет, то еще раз эту команду повторить

#### Создаем БД
Запустить MySQL:
```
sudo /etc/init.d/mysql start
```
Авторизоваться под пользователем root:
```
mysql -u root
```
Создать базу данных 'database':
```
CREATE DATABASE database_db;
```
Выходим из mysql:
```
exit
```
Проверить что в настройках django проекта нужна БД:
```
nano web/ask/ask/settings.py
``` 
```python
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'database_db',
    'USER': 'root',
    'HOST': '127.0.0.1',
    'PORT': '3306',
}
```
Накатить таблицы в эту базу данных:
```
cd web/ask
# python3 manage.py makemigrations
python3 manage.py migrate
```
Проверить что есть таблицы
```
mysql -u root
use database_db;
show tables;
```
Проверим запускается ли приложение
```
cd web/ask
python3 manage.py runserver
```
#### Установка nginx и запуск приложения
Создаем ссылку конфига nginx и запускаем его
```
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx start
```
Запускаем приложения
```
cd /home/box/web
gunicorn -c /home/box/web/etc/hello.py hello:app &

cd /home/box/web/ask
gunicorn -c /home/box/web/etc/ask.py ask.wsgi &
```
Проверяем что работает
```
curl http://127.0.0.1/hello/?a=bcd
curl http://127.0.0.1/login/
```
Чтобы перезагрузить сервер нужно выполнить:
```
sudo reload gunicorn
```
Или так:
```
fg 2
Ctrl+C
gunicorn -c /home/box/web/etc/ask.py ask.wsgi --daemon
```
