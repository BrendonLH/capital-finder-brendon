from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    """[Purpose]: parses out the url to get the query
    [Format]: /api/app?(argument)=(argument)
    [Arguments]: country=country name, capital=capital name
    [Example]: /api/app?country=Peru"""
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        print(url_components)
        dic = dict(query_string_list)
        print(dic)

        # url and other vars used across the app

        # specification for URL parse for country lookup
        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            print(data)
            capital = ""
            for cap in data:
                country_capital = cap["capital"][0]
                capital += country_capital
            message = f'capital of {dic["country"]} is {capital} '

        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            print(data)
            country = ''
            for count in data:
                country_capital = str(count["name"]["common"])
                print(country_capital)
                country += country_capital
            message = f'The capital of {country} is {dic["capital"]}'

        else:
            message = "Select A Country or A Capital"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
