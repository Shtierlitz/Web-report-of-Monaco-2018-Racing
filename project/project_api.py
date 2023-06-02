# project/project_api.py

from flask_restful import Api, Resource
from flask import request, jsonify, Response
from dicttoxml2 import dicttoxml
from project.new_report import *
from project.models import *

api = Api()

template = {
    "info": {
        "description": "Shtierlitz",
        "version": "'1.0.0",
        "title": "Shtierlitz's-Web-report-of-Monaco-2018-Racing-API",
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


class ApiReport(Resource):
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

        rep_asc = OriginReport.select().order_by(OriginReport.duration.asc())
        lst_ask = js_data_base_list(rep_asc)
        if response_format == "json":
            if order == "desc":
                rep_desc = OriginReport.select().order_by(OriginReport.duration.desc())
                lst_desc = js_data_base_list(rep_desc)
                return jsonify(lst_desc)
            return jsonify(lst_ask)
        elif response_format == "xml":
            xml_ask = dicttoxml(rep_asc.dicts().execute()).decode()
            if order == "desc":
                rep_desc = OriginReport.select().order_by(OriginReport.duration.desc())
                xml_desk = dicttoxml(rep_desc.dicts().execute()).decode()
                return Response(xml_desk, mimetype='text/xml')
            return Response(xml_ask, mimetype='text/xml')
        elif order == "desc":
            rep_desc = OriginReport.select().order_by(OriginReport.duration.desc())
            lst_desc = js_data_base_list(rep_desc)
            if response_format == 'json':
                lst_desc = js_data_base_list(rep_desc)
                return jsonify(lst_desc)
            elif response_format == "xml":

                xml_desk = dicttoxml(rep_desc.dicts().execute()).decode()
                return Response(xml_desk, mimetype='text/xml')
            return jsonify(lst_desc)
        return jsonify(lst_ask)


api.add_resource(ApiReport, "/api/v1/report/")
