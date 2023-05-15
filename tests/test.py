from unittest import TestCase, main
import requests


class TestApi(TestCase):

    def test_main_page(self):
        response = requests.get("http://127.0.0.1:5000/api/v1/report/")
        assert response.status_code == 200
        assert len(response.json()) == 19

    def test_order_ask(self):
        response = requests.get("http://127.0.0.1:5000/api/v1/report/?order=asc")
        assert response.status_code == 200
        js = response.json()
        assert {'abbr': 'SVF', 'duration': '0:01:04.415000', 'end': '2018-05-24 12:04:03.332000',
                'name': 'Sebastian Vettel', 'start': '2018-05-24 12:02:58.917000', 'team': 'FERRARI'} == js[0]
        assert {'abbr': 'DRR', 'duration': '23:57:12.013000', 'end': '2018-05-24 12:11:24.067000',
                'name': 'Daniel Ricciardo', 'start': '2018-05-24 12:14:12.054000',
                'team': 'RED BULL RACING TAG HEUER'} == js[-1]

    def test_order_desc(self):
        response = requests.get("http://127.0.0.1:5000/api/v1/report/?order=desc")
        assert response.status_code == 200
        js = response.json()
        assert {'abbr': 'DRR', 'duration': '23:57:12.013000', 'end': '2018-05-24 12:11:24.067000',
                'name': 'Daniel Ricciardo', 'start': '2018-05-24 12:14:12.054000',
                'team': 'RED BULL RACING TAG HEUER'} == js[0]
        assert {'abbr': 'SVF', 'duration': '0:01:04.415000', 'end': '2018-05-24 12:04:03.332000',
                'name': 'Sebastian Vettel', 'start': '2018-05-24 12:02:58.917000', 'team': 'FERRARI'} == js[-1]

    def test_format_json(self):
        response = requests.get("http://127.0.0.1:5000/api/v1/report/?format=json")
        assert response.status_code == 200
        js = response.json()
        assert {'abbr': 'SVF', 'duration': '0:01:04.415000', 'end': '2018-05-24 12:04:03.332000',
                'name': 'Sebastian Vettel', 'start': '2018-05-24 12:02:58.917000', 'team': 'FERRARI'} == js[0]
        assert {'abbr': 'DRR', 'duration': '23:57:12.013000', 'end': '2018-05-24 12:11:24.067000',
                'name': 'Daniel Ricciardo', 'start': '2018-05-24 12:14:12.054000',
                'team': 'RED BULL RACING TAG HEUER'} == js[-1]

    def test_format_xml(self):
        response = requests.get("http://127.0.0.1:5000/api/v1/report/?format=xml")
        assert response.status_code == 200
        assert '?xml version="1.0" encoding="UTF-8"' in response.content.decode()
        assert response.headers['Content-Type'] == 'text/xml; charset=utf-8'


if __name__ == '__main__':
    main()
