# web-stepik

####  лонируем репозиторий
    git clone https://github.com/Auerbah/web-stepik
    mv web-stepik/web ~/

#### ”станавливаем django нужной версии, иначе проект не будет запускатьс€
        sudo pip3 install Django==2.0

возможно процесс не будет завершатьс€, тогда нужно прервать процесс и проверить установилс€ ли django версии 2.0,
если нет, то еще раз эту команду повторить

#### ѕроверим запускаетс€ ли приложение
cd web/ask
python3 manage.py runserver

#### —оздаетм ссылку конфига nginx и запускаем его
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo sudo /etc/init.d/nginx start

#### «апускаем приложени€
cd /home/box/web
gunicorn -c /home/box/web/etc/hello.py hello:app &

cd /home/box/web/ask
gunicorn -c /home/box/web/etc/ask.py ask.wsgi &

#### ѕровер€ем что работает
curl http://127.0.0.1/hello/?a=bcd
curl http://127.0.0.1/login/