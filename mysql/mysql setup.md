����� ����������� ����������� ����� ��������� ��������� �������:

1) ��������� MySQL:
    sudo /etc/init.d/mysql start

2) �������������� ��� ������������� root:
    mysql -u root

3) ������� ���� ������ 'database':
    CREATE DATABASE database_db;

4) ����� �� mysql:
   exit

5) ������������� django ������ ������, ����� ������ �� ����� �����������
    sudo pip3 install Django==2.0

�������� ������� �� ����� �����������, ����� ����� �������� ������� � ��������� ����������� �� django ������ 2.0,
���� ���, �� ��� ��� ��� ������� ���������
    

6) �������� ������� � ��� ���� ������:
    cd web/ask
    python3 manage.py migrate
    python3 manage.py makemigrations

7) ��������� ��� ���� �������
    mysql -u root
    use database_db;
    show tables;