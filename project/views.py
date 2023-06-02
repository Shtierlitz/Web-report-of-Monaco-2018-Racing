# project/views.py
from flask import render_template, request, Blueprint, abort
from project.models import *

report_bp = Blueprint('drivers', __name__)
error_bp = Blueprint('errors', __name__)


@report_bp.route('/report/')
def report():
    query = OriginReport.select().order_by(OriginReport.duration.asc())

    return render_template('report.html', title="Monako racing report", report=query)


@report_bp.route('/report/drivers/')
def drivers():
    order = request.args.get('order')
    driver_id = request.args.get('driver_id')

    if driver_id:
        driver = OriginReport.get(OriginReport.abbr == driver_id)
        if driver is not None:
            return render_template('driver.html', title=f"Info for driver: {driver_id}",
                                   driver=driver)
        elif driver is None:
            return abort(404)
    if order:
        if order == "desc":
            flag = True
            return render_template('drivers.html', title="Monako racing report",
                                   drivers=OriginReport.select().order_by(OriginReport.duration.desc()), fl=flag)

    return render_template('drivers.html', title="Monako racing report",
                           drivers=OriginReport.select().order_by(OriginReport.duration.asc()))


@report_bp.route('/report/drivers/<drivername>')
def driver(drivername):
    racer = OriginReport.get(OriginReport.abbr == drivername)
    if racer is None:
        return abort(404)
    return render_template('driver.html', title=f"Info for driver: {drivername}",
                           driver=racer)


@error_bp.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404
