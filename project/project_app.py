from flask import Flask
from flasgger import Swagger
from project.views import *
from project.project_api import *
from project.models import data_base


def create_app(config):
    app = Flask(__name__)
    if config == 'development':
        app.config.from_pyfile("local_settings.py")
    elif config == 'testing':
        app.config.from_pyfile('testing_settings.py')

    app.register_blueprint(report_bp)
    app.register_blueprint(error_bp)

    swagger = Swagger(app, template=template)

    api.init_app(app)

    db_sq = SqliteDatabase(app.config['DATA_BASE'])
    data_base.initialize(db_sq)

    return app


if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True)
