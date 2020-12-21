from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app =  Flask('__name__')

app.config.from_object('config')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

conn = MySQLdb.connect(
    user = 'dev',
    password = 'secret',
    db = 'flask',
    host = 'localhost',
    port = 3306
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:secret@localhost/flask'
# or SQL lite
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


from app.models import tables
from app.controllers import router
