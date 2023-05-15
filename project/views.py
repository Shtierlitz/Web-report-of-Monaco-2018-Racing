from project.new_report import *
from flask import render_template, request, Blueprint, abort, current_app

report_bp = Blueprint('drivers', __name__)
error_bp = Blueprint('errors', __name__)


@report_bp.route('/report/')
def report():
    build = build_report(current_app.config['DATA_DIR'])
    return render_template('report.html', title="Monako racing report", report=sort_report(build, 'asc').items())


@report_bp.route('/report/drivers/')
def drivers():
    build = build_report(current_app.config['DATA_DIR'])

    order = request.args.get('order')
    driver_id = request.args.get('driver_id')

    if driver_id:
        driver = find_driver_by_abbr(build, driver_id)
        if driver is not None:
            return render_template('driver.html', title=f"Info for driver: {driver_id}",
                                   driver=driver)
        elif driver is None:
            return abort(404)
    if order:
        if order == "desc":
            flag = True
            return render_template('drivers.html', title="Monako racing report",
                                   drivers=sort_report(build, 'desc').items(), fl=flag)

    return render_template('drivers.html', title="Monako racing report", drivers=sort_report(build, 'asc').items())


@report_bp.route('/report/drivers/<drivername>')
def driver(drivername):
    build = build_report(current_app.config['DATA_DIR'])
    racer = find_driver_by_abbr(build, drivername)
    if racer is None:
        return abort(404)
    return render_template('driver.html', title=f"Info for driver: {drivername}",
                           driver=racer)


@error_bp.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404
