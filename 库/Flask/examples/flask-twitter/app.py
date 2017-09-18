import datetime

from hashlib import md5
from functools import wraps

import flask, peewee
from db import User, Message, Relationship, database

# 配置
DEBUG = True
SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'

# 创建应用，添加配置
app = flask.Flask(__name__)
app.config.from_object(__name__)

# 设置用户信息到session
def auth_user(user):
    flask.session['logged_in'] = True
    flask.session['user_id'] = user.id
    flask.session['username'] = user.username
    flask.flash('You are logged in as %s' % (user.username))

# 获取当前用户
def get_current_user():
    if flask.session.get('logged_in'):
        return User.get(User.id == flask.session['user_id'])

# 判断是否已登录
def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not flask.session.get('logged_in'):
            return flask.redirect(flask.url_for('login'))
        return f(*args, **kwargs)
    return inner

# 限制显示数目
def object_list(template_name, qr, var_name='object_list', **kwargs):
    kwargs.update(
        page = int(flask.request.args.get('page', 1)),
        pages = qr.count()/20 + 1
    )
    kwargs[var_name] = qr.paginate(kwargs['page'])
    return flask.render_template(template_name, **kwargs)

# 获取用户或返回404
def get_object_or_404(model, *expressions):
    try:
        return model.get(*expressions)
    except model.DoesNotExist:
        flask.abort(404)

# 添加过滤器，判断是否关注特定用户
@app.template_filter('is_following')
def is_following(from_user, to_user):
    return from_user.is_following(to_user)

# 前处理
@app.before_request
def before_request():
    try:
        flask.g.db = database
        flask.g.db.connect()
    except:
        pass

# 后处理
@app.after_request
def after_request(response):
    flask.g.db.close()
    return response

# 首页
@app.route('/')
def homepage():
    if flask.session.get('logged_in'):
        return private_timeline()
    else:
        return public_timeline()

# 个人首页，私人推送
@app.route('/private/')
def private_timeline():
    user = get_current_user()
    messages = Message.select().where(Message.user << user.following())
    return object_list('private_messages.html', messages, 'message_list')

# 公共推送
@app.route('/public/')
def public_timeline():
    messages = Message.select()
    return object_list('public_messages.html', messages, 'message_list')

# 创建用户
@app.route('/join/', methods=['GET', 'POST'])
def join():
    if flask.request.method == 'POST' and flask.request.form['username']:
        try:
            with database.transaction():
                user = User.create(
                    username = flask.request.form['username'],
                    password = md5((flask.request.form['password']).encode('utf-8')).hexdigest(),
                    email = flask.request.form['email'],
                    join_date = datetime.datetime.now()
                )
            auth_user(user)
            return flask.redirect(flask.url_for('homepage'))
        except peewee.IntegrityError:
            flask.flash('That username is already taken')

    return flask.render_template('join.html')

# 登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        if not flask.request.form['username'] or not flask.request.form['password']:
            flask.flash('Username or password is blank')
        else:
            try:
                user = User.get(
                    username = flask.request.form['username'],
                    password = md5(flask.request.form['password'].encode('utf-8')).hexdigest()
                )
            except User.DoesNotExist:
                flask.flash('Username or password entered is incorrect')
            else:
                auth_user(user)
                return flask.redirect(flask.url_for('homepage'))

    return flask.render_template('login.html')

# 登出
@app.route('/logout/')
def logout():
    flask.session.pop('logged_in', None)
    flask.flash('You were logged out')
    return flask.redirect(flask.url_for('homepage'))

# 个人关注列表
@app.route('/following/')
@login_required
def following():
    user = get_current_user()
    return object_list('user_following.html', user.following(), 'user_list')

# 个人被关注列表
@app.route('/followers/')
@login_required
def followers():
    user = get_current_user()
    return object_list('user_followers.html', user.followers(), 'user_list') 

# 用户列表
@app.route('/users/')
def user_list():
    users = User.select()
    return object_list('user_list.html', users, 'user_list') 

# 用户详情页
@app.route('/users/<username>/')
def user_detail(username):
    user = get_object_or_404(User, User.username == username)
    messages = user.message_set
    return object_list('user_detail.html', messages, 'message_list', user=user)

# 关注用户
@app.route('/users/<username>/follow/', methods=['POST'])
@login_required
def user_follow(username):
    user = get_object_or_404(User, User.username == username)
    try:
        with database.transaction():
            Relationship.create(
                from_user = get_current_user(),
                to_user = user
            )
    except peewee.IntegrityError:
        pass

    flask.flash('You are following %s' % user.username)
    return flask.redirect(flask.url_for('user_detail', username=user.username))

# 取消关注
@app.route('/users/<username>/unfollow/', methods=['POST'])
@login_required
def user_unfollow(username):
    user = get_object_or_404(User, User.username == username)
    Relationship.delete().where(
        Relationship.from_user == get_current_user() &
        Relationship.to_user == user
    ).execute()
    flask.flash('You are no longer following %s' % user.username)
    return flask.redirect(flask.url_for('user_detail'), username=user.username)

# 创建信息
@app.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    user = get_current_user()
    if flask.request.method == 'POST' and flask.request.form['content']:
        Message.create(
            user=user,
            content=flask.request.form['content'],
            pub_date=datetime.datetime.now())
        flask.flash('Your message has been created')
        return flask.redirect(flask.url_for('user_detail', username=user.username))

    return flask.render_template('create.html')

# 上下文处理器
@app.context_processor
def _inject_user():
    return {'current_user': get_current_user()}

if __name__ == '__main__':
    app.run()
