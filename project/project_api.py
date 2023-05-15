from flask_restful import Api, Resource
from flask import request, jsonify, Response, current_app
from dicttoxml2 import dicttoxml
from project.new_report import *

api = Api()

template = {
    "info": {
        "description": "Shtierlitz",
        "version": "'1.0.0",
        "title": "Shtierlitz's-Python-Flask-REST-task-8",
        "contact": {
            "email": "rollbar1990@gmail.com"
        },
        "license": {
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT"
        },
        "host": "localhost",
        "basePath": "api",
        "schemes": ["http", "https"],
        "operationID": "getmyreport"
    },
    "swagger": "2.0",
    "paths": {}
}


class Api_Report(Resource):
    def get(self):
        """Returns the statistics of the Monaco 2018 Racing
                   ---
                   parameters:
                     - name: format
                       in: query
                       type: string
                       enum: ["json", "xml"]
                       required: false
                       default: "json"
                     - name: order
                       in: query
                       type: string
                       enum: ["desc"]
                       required: false
                       default: "asc"
                   responses:
                     200:
                       description: OK
                     404:
                       description: Not found
                     505:
                       description: Internal server error
                   produces:
                     - application/json
                     - application/xml
                   """
        response_format = request.args.get('format')
        order = request.args.get('order')

        build = build_report(current_app.config['DATA_DIR'])
        rep_ask = sort_report(build, 'asc')
        lst_ask = js_list(rep_ask)
        if response_format == "json":
            if order == "desc":
                rep_desk = sort_report(build, "desc")
                lst_desk = js_list(rep_desk)
                return jsonify(lst_desk)
            return jsonify(lst_ask)
        elif response_format == "xml":
            xml_ask = dicttoxml(rep_ask).decode()
            if order == "desc":
                rep_desk = sort_report(build, "desc")
                xml_desk = dicttoxml(rep_desk).decode()
                return Response(xml_desk, mimetype='text/xml')
            return Response(xml_ask, mimetype='text/xml')
        elif order == "desc":
            rep_desk = sort_report(build, "desc")
            lst_desk = js_list(rep_desk)
            if response_format == 'json':
                lst_desk = js_list(rep_desk)
                return jsonify(lst_desk)
            elif response_format == "xml":

                xml_desk = dicttoxml(rep_desk).decode()
                return Response(xml_desk, mimetype='text/xml')
            return jsonify(lst_desk)
        return jsonify(lst_ask)
