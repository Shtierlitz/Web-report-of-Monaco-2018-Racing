from flask import current_app, g, Blueprint
import sqlite3
import os

app_blueprint = Blueprint('app', __name__)


DATA_BASE = 'racers.db'

def create_db():
    db = connect_bd()
    with app_blueprint.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def connect_bd():
    conn = sqlite3.connect(database=DATA_BASE)
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    if not hasattr(g, 'link_bd'):
        g.link_db = connect_bd()
    return g.link_db
