Работа с БД в MySQL

Установить БД:

Запустить БД:
```
$ sudo /etc/init.d/mysql start
```
Авторизоваться под пользователем root:
```
$ mysql -u root
```
В случае наличия пароля:
```
$ mysql -u root -p
```
Создать базу данных 'database':
```
mysql> CREATE DATABASE database_db;
```
Список всех баз данных можно посмотреть используя:
```
mysql> SHOW SCHEMAS;
```
Выбрать database_db для использования:
```
mysql> USE database_db;
```
Посмотреть список всех таблиц:
```
mysql> SHOW TABLES;
```
Если таблиц нет, то вернется: `Empty set (0.00 sec)`

Создать таблицу user:
```
mysql> CREATE TABLE user (name VARCHAR(20), email VARCHAR(20), password VARCHAR(20));
```
Проверим описание созданной таблицы:
```
mysql> DESCRIBE user;
```
Добавим нового пользователя:
```
mysql> INSERT INTO user VALUES ('Alex', 'alex@gmail.com', NULL);
```
Посмотрим таблицу:
```
mysql> SELECT * FROM user;
```
Добавим данные из файла. Для этого запишем в файл users.txt следующие строки:
```
Stas	\N	\N
Vlad	vlad@gmail.com	password
```
Здесь каждая строка будет соответсвовать новой ячейке таблицы, каждый атрибут должен быть отделен табуляцией, а для значений NULL можно использовать \N
Если файл сохраняется на Windows, то его нужно сохранять в формате ANSI

Для загрузки используем следующие команды:
Linux:
```
mysql> LOAD DATA LOCAL INFILE '/path/users.txt' INTO TABLE user;
```
Windows:
```
mysql> LOAD DATA LOCAL INFILE '/path/users.txt' INTO TABLE user LINES TERMINATED BY '\r\n';
```
Загруженные данные добавятся в конец существующей таблицы

Проверяем:
```
mysql> SELECT * FROM user;
```
Для удаления ячейки используем:
```
mysql> DELETE FROM user WHERE name = 'Vlad';
```
