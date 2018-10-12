# -*- coding: utf-8 -*-
# @Time    : 18-9-30 上午11:09
# @Author  : allen.you
import datetime

from flask import Flask, request, render_template, url_for, make_response
import os

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename, redirect

from config import Config
from flask_script import Manager, Server

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLA
api = Api(app)


@app.route('/')
def index():
    # 读取cookie
    # username = request.cookies.get('username')

    return redirect(url_for('login'))


@app.errorhandler(404)
@app.route('/user/')
@app.route('/user/<username>/')
def user(username):
    return render_template('user.html',
                           name=username,
                           current_time=datetime.datetime.utcnow())


@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The Projects Page'


@app.route('/about')
def about():
    return 'The About'


#
# @app.route('/login/', methods=['POST', "GET"])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return login_the_user(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     return render_template('login.html', error=error)

#
# @app.error_handler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404
#
#
# @app.error_handler(404)
# def page_not_found(error):
#     resp = make_response(render_template('page_not_found.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp


@app.route('/upload_file', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class TaskListAPI(Resource):
    def get(self):
        pass

    def put(self):
        pass


class TaskAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')


if __name__ == '__main__':
    manager.add_command("runserver", Server(ssl_crt=os.path.join(Config.ROOT_DIR, 'server.crt'),
                                            ssl_key=os.path.join(Config.ROOT_DIR, 'server.key')))
    manager.run()
    # app.run(host='127.0.0.1', debug=True, port=8100,
    #         ssl_context=(os.path.join(config.ROOT_DIR, 'server.crt'),
    #                      os.path.join(config.ROOT_DIR, 'server.key')))
