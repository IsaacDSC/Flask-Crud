

1 - pip install Flask

2 - created virtualenv

3 - insert command = myEnv/bin/pip3 freeze > requirements.txt
    #insert frames instaled in pip3 in file requirements.txt

4 - definition arquiteture of patterns Flask
    create file __init__.py  == settings or server.js, configuration
    files inside folder app
    folder controllers,  created file __init__.py
    folder models, created file __init__.py
    folder templates => organization pattern views html
    folder static => organization pattern folder of css, js, img etc

5 - install ORM
    #myEnv/bin/pip3 install flask-sqlalchemy

6 - install conn mysqk db
    #myEnv/bin/pip3 install flask_mysqldb==0.2.0

7 - install flask migrate addictions commands of terminal if true change
    #pip3 install flask-migrate
    #pip3 install flask-script

8 - command - creating folder migrations
    #python3 run.py db init

9 - command - initialing migrations in migrate db = created file storage.db automatic
    #python3 run.py db migrate

10 - command - apply migrations
    #python3 run.py db upgrade


11 -  download flask_wtf for create templates froms flask
    #pip3 install flask-wtf


OBS => ATUALIZAR A PAGINA RESETANDO COMMAND = ALT + F5
OBS => CRIAR UMA SEGUNDA  MODELS, MODIFICANDO PARA MYSQL