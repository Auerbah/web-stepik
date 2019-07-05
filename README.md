# web-stepik

#### ��������� �����������
    git clone https://github.com/Auerbah/web-stepik
    mv web-stepik/web ~/

#### ������������� django ������ ������, ����� ������ �� ����� �����������
        sudo pip3 install Django==2.0

�������� ������� �� ����� �����������, ����� ����� �������� ������� � ��������� ����������� �� django ������ 2.0,
���� ���, �� ��� ��� ��� ������� ���������

#### �������� ����������� �� ����������
cd web/ask
python3 manage.py runserver

#### �������� ������ ������� nginx � ��������� ���
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo sudo /etc/init.d/nginx start

#### ��������� ����������
cd /home/box/web
gunicorn -c /home/box/web/etc/hello.py hello:app &

cd /home/box/web/ask
gunicorn -c /home/box/web/etc/ask.py ask.wsgi &

#### ��������� ��� ��������
curl http://127.0.0.1/hello/?a=bcd
curl http://127.0.0.1/login/