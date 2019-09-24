Работа с БД в MySQL

0) Установить БД:

1) Запустить БД:
    $ sudo /etc/init.d/mysql start

2) Авторизоваться под пользователем root:
    $ mysql -u root
В случае наличия пароля:
    $ mysql -u root -p

3) Создать базу данных 'database':
    mysql> CREATE DATABASE database_db;

4) Спиоск всех баз данных можно посмотерть используя:
    mysql> SHOW SCHEMAS;

5) Выбрать database_db для использования:
    mysql> USE database_db;

6) Посмотреть список всех таблиц:
    mysql> SHOW TABLES;
Если таблиц нет, то вернется: Empty set (0.00 sec)

7) Создать таблицу user:
    mysql> CREATE TABLE user (name VARCHAR(20), email VARCHAR(20), password VARCHAR(20));

8) Проверим описание созданной таблицы:
   mysql> DESCRIBE user;

9) Добавим нового пользователя:
    mysql> INSERT INTO user VALUES ('Alex', 'alex@gmail.com', NULL);

10) Посмотрим таблицу:
    mysql> SELECT * FROM user;

11) Добавим данные из файла. Для этого запишем в файл users.txt следующие строки:
Stas	\N	\N
Vlad	vlad@gmail.com	password

Здесь каждая строка будет соответсвовать новой ячейке таблицы, каждый атрибут должен быть отделен табуляцией, а для значений NULL можно использовать \N
Если файл сохраняется на Windows, то его нужно сохранять в формате ANSI

Для загрузки используем следующие команды:
Linux:
    mysql> LOAD DATA LOCAL INFILE '/path/users.txt' INTO TABLE user;
Windows:
    mysql> LOAD DATA LOCAL INFILE '/path/users.txt' INTO TABLE user LINES TERMINATED BY '\r\n';

Загруженные данные добавятся в конец существующей таблицы

12) Проверяем:
    mysql> SELECT * FROM user;

13) Для удаления ячейки используем:
    mysql> DELETE FROM user WHERE name = 'Vlad';


