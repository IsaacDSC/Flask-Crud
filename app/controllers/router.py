from flask import render_template
from app import app, db
from app.models.forms import LoginForm
from app.models.tables import User
from app.models.SQL import conn

@app.route('/index')
@app.route('/')
def home():
    datas = ['isaac', 'raissa']
    return render_template('index.html', datas=datas)


@app.route('/test')
@app.route('/test/<name>')
# if number <int: id>
def test(name=None):
    if name:
        return 'Olá, %s!' % name
    else:
        return 'Ola!'


@app.route('/limit', methods=['GET'])
# limit methods
def limit():
    return 'Limit Get URL'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

    return render_template('login.html', form=form)


@app.route('/insert')
def insert():
    i = User('isaacdsc', '123456', 'Isaac', 'isaac8.silva@hotmail.com')
    db.session.add(i)
    db.session.commit()
    return 'ok'


@app.route('/selectby')
def selectby():
    i = User.query.filter_by(username='isaacdsc').all()
    print(i[0].username)
    return 'ok'


@app.route('/update')
def update():
    i = User.query.filter_by(username='isaacdsc').first()
    i.name = 'IsaacDSC'
    db.session.add(i)
    db.session.commit()
    return 'ok'


@app.route('/delete')
def dell():
    i = User.query.filter_by(username='isaacdsc').first()
    db.session.delete(i)
    db.session.commit()
    return 'ok'

@app.route('/selectmysql')
def select():
    query = 'SELECT * FROM users;'
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    #print(cursor)
    for users in cursor.fetchall():
        print(users)
    return 'ok'


