ѕосле копировани€ репозитори€ нудно выполнить следующие команды:

1) «апустить MySQL:
    sudo /etc/init.d/mysql start

2) јвторизоватьс€ под пользователем root:
    mysql -u root

3) —оздать базу данных 'database':
    CREATE DATABASE database_db;

4) ¬ыйти из mysql:
   exit

5) ”станавливаем django нужной версии, иначе проект не будет запускатьс€
    sudo pip3 install Django==2.0

возможно процесс не будет завершатьс€, тогда нужно прервать процесс и проверить установилс€ ли django версии 2.0,
если нет, то еще раз эту команду повторить
    

6) Ќакатить таблицы в эту базу данных:
    cd web/ask
    python3 manage.py migrate
    python3 manage.py makemigrations

7) ѕроверить что есть таблицы
    mysql -u root
    use database_db;
    show tables;