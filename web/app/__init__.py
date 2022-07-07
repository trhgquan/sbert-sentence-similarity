'''Init a Flask app
'''

import os
from flask import Flask, make_response, render_template
from flask_restful import Api

from .module.pipeline import Pipeline

def create_app(test_config = None):
    '''Create a new app with test_config
    '''

    app = Flask(__name__, instance_relative_config = True)

    app.config.from_mapping(
        SECRET_KEY = '1337'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api = Api(app)
    api.add_resource(Pipeline, '/score', endpoint = 'score')

    @app.route('/')
    def index():
        return render_template('html/index.html')

    @app.route('/index.js')
    def index_js():
        response = make_response(render_template('js/index.js'))
        response.headers['Content-type'] = 'text/javascript'
        return response

    @app.route('/utils.js')
    def utils_js():
        response = make_response(render_template('js/utils.js'))
        response.headers['Content-type'] = 'text/javascript'
        return response

    return app
