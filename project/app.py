from flask import Flask, current_app
from flasgger import Swagger
from project.views import *
from project.project_api import *

app = Flask(__name__)
app.config.from_pyfile("local_settings.py")



app.register_blueprint(report_bp)
app.register_blueprint(error_bp)

swagger = Swagger(app, template=template)

api.add_resource(Api_Report, "/api/v1/report/")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
