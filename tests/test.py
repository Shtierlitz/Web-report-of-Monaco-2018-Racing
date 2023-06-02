# tests/test.py

from project.app import *
from project.db_create_script import *
import pytest


@pytest.fixture()
def app():
    app = create_app('testing')
    init_db(app.config['DATA_BASE'])
    fill_db(app.config['DATA_DIR'])

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_main_api_page(client):
    response = client.get("/api/v1/report/")
    assert response.status_code == 200
    assert len(response.get_json()) == 19


def test_order_ask(client):
    response = client.get("/api/v1/report/?order=asc")
    assert response.status_code == 200
    js = response.get_json()
    assert {'abbr': 'SVF', 'duration': '0:01:04.415000', 'end': '2018-05-24 12:04:03.332000',
            'name': 'Sebastian Vettel', 'start': '2018-05-24 12:02:58.917000', 'team': 'FERRARI'} == js[0]
    assert {'abbr': 'DRR', 'duration': '23:57:12.013000', 'end': '2018-05-24 12:11:24.067000',
            'name': 'Daniel Ricciardo', 'start': '2018-05-24 12:14:12.054000',
            'team': 'RED BULL RACING TAG HEUER'} == js[-1]


def test_order_desc(client):
    response = client.get("/api/v1/report/?order=desc")
    assert response.status_code == 200
    js = response.get_json()
    assert {'abbr': 'DRR', 'duration': '23:57:12.013000', 'end': '2018-05-24 12:11:24.067000',
            'name': 'Daniel Ricciardo', 'start': '2018-05-24 12:14:12.054000',
            'team': 'RED BULL RACING TAG HEUER'} == js[0]
    assert {'abbr': 'SVF', 'duration': '0:01:04.415000', 'end': '2018-05-24 12:04:03.332000',
            'name': 'Sebastian Vettel', 'start': '2018-05-24 12:02:58.917000', 'team': 'FERRARI'} == js[-1]


def test_format_json(client):
    response = client.get("/api/v1/report/?format=json")
    js = response.get_json()
    assert {'abbr': 'SVF', 'duration': '0:01:04.415000', 'end': '2018-05-24 12:04:03.332000',
            'name': 'Sebastian Vettel', 'start': '2018-05-24 12:02:58.917000', 'team': 'FERRARI'} == js[0]
    assert {'abbr': 'DRR', 'duration': '23:57:12.013000', 'end': '2018-05-24 12:11:24.067000',
            'name': 'Daniel Ricciardo', 'start': '2018-05-24 12:14:12.054000',
            'team': 'RED BULL RACING TAG HEUER'} == js[-1]


def test_format_xml(client):
    response = client.get("/api/v1/report/?format=xml")
    assert response.status_code == 200
    assert '?xml version="1.0" encoding="UTF-8"' in response.data.decode()
    assert response.headers['Content-Type'] == 'text/xml; charset=utf-8'
