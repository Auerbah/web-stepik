После копирования репозитория нужно выполнить следующие команды:

Запустить MySQL:
```
$ sudo /etc/init.d/mysql start
```
Авторизоваться под пользователем root:
```
$ mysql -u root
```
Создать базу данных 'database':
```
mysql> CREATE DATABASE database_db;
```
Выйти из mysql:
```
exit
```
Устанавливаем django нужной версии, иначе проект не будет запускаться
```
$ sudo pip3 install Django==2.0
```
Возможно процесс не будет завершаться, тогда нужно прервать процесс и проверить установился ли django версии 2.0,
если нет, то еще раз эту команду повторить
    
Накатить таблицы в эту базу данных:
```
$ cd web/ask
$ python3 manage.py migrate
$ python3 manage.py makemigrations
```
Проверить, что есть таблицы
```
$ mysql -u root
mysql> use database_db;
mysql> show tables;
```