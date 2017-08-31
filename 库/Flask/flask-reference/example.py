import flask
from flask import Flask, url_for, render_template, request, make_response, redirect, abort
from werkzeug import secure_filename


# 创建一个Flask应用
app = Flask(__name__)

# 通过环境变量加载配置文件
app.config.from_envvar('FLASKR_SETTINGS', silent=True)  # 如果没有这个变量，不会报错
# 通过给定加载配置
app.config.from_object(__name__)    # 加载这个文件


# 在第一个请求之前执行，一个应用只执行一次
@app.before_first_request
def before_first_request():
    print('before_first_request')


# 每个请求之前执行
@app.before_request
def before_request():
    print('before_request')


# 每个请求最后执行，最后要返回响应
@app.after_request
def after_request(response):
    print('after_request')
    return response


# 映射路由'/'到方法hello
@app.route('/')
def hello():
    print('hello')
    return 'Hello world'


# 映射路由'/hello/<name>'到方法hello_name, name为变量, 方法名不能与其它路由相同
@app.route('/hello/<name>')
def hello_name(name):
    print('hello_name %s' % name)
    return 'Hello_name %s' % name


# URL最后有没有/是完全不一样的
@app.route('/hello/<name>/')
def hello_name_with_slash(name):
    print('hello_name_with_slash %s' % name)
    return 'Hello_name_with_slash %s' % name


# 可以在变量前面添加转换器，格式为<converter:variable_name>，包括以下转换器：
'''
string      默认值，接受除/以外的任何字符
int         接受数字，转换为整型
float       接受数字，转换为浮点型
path        接受任何字符包括/
any
uuid
'''
@app.route('/id/<int:id>')
def hello_id(id):
    # 当id不为数字时，会显示requested url was not found
    print('hello_id %d' % id)
    return 'Hello_id %d' % id


# test_request_context用于激活一个临时的请求上下文，可以访问 request 、g 和 session 对象
@app.route('/test')
def test():
    with app.test_request_context():
        print(url_for('hello')) # url_for的第一个参数为方法名,后面为这个方法所需的参数，返回对应的URL
        print(url_for('hello_name', name='test'))
        print(url_for('hello_id', id=123))
    return 'test'

# 常用于测试
with app.test_request_context('/test2', method='POST'):
    assert request.path == '/test2'
    assert request.method == 'POST'


# 静态文件
# 可以直接访问/static/static.html，默认设置是当前文件夹内的static文件夹


# 使用模板，默认模板文件夹是templates
@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name=None):
    return render_template('hi.html', name=name)    # 用render_template来渲染Jinja2模板，在模板内可以使用config, request, session, g对象和get_flashed_messages, url_for方法


# 为g添加变量
@app.context_processor
def context_var():
    return dict(test='test123')


# method用于指定接受单个的方法,methods接受一个列表
# method包括GET, HEAD, POST, PUT, DELETE, OPTIONS
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # 通过request.form获取POST内容，如果不存在这个键，则会抛出KeyError
        if valid_login(request.form['username'], request.form['password']):
            pass
        else:
            error = 'Login fail'
    if request.method == 'GET':
        param = request.args.get('key', '') # 通过request.args.get方法获取参数值
        error = 'Login fail and param key is ' + param
    return render_template('login.html', error=error)


# 文件上传
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        #f = request.files['the_file']
        #print(secure_filename(f.filename))
        #f.save('temp/' + secure_filename(f.filename))
        pass
    else:
        return render_template('upload_file.html')


# Cookie
@app.route('/get_cookie', methods=['GET'])
def get_cookie():
    username = request.cookies.get('username')  # 用request.cookies.get来获取cookie值
    if username:
        return username
    return 'no cookie'

@app.route('/set_cookie', methods=['GET'])
def set_cookie():
    resp = make_response('set cookie')  # 把字符串转换为响应对象
    resp.set_cookie('username', 'test') # 设置cookie
    return resp


# 重定向
@app.route('/redirect')
def redirect_test():
    return redirect(url_for('get_401'))   # 重定向至'/error'


# 抛出错误页面
@app.route('/error')
def get_401():
    abort(401)  # 抛出401错误
    print('test')   # 不会执行


# 定制错误页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# 修改相应,使用make_response来包裹原来的对象，再设置响应
@app.route('/sp_header')
def sp_header():
    resp = make_response('sp_header')
    resp.headers['test'] = 'A sp value'
    return resp


# 日志
@app.route('/logger')
def set_log():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return 'set log'


if __name__ == '__main__':
    # 使用debug模式
    app.run(debug=True)