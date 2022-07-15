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
        url = "https://restcountries.com/v3.1/name/"

        # specification for URL parse for country lookup
        if "country" in dic:
            r = requests.get(url + dic["country"])
            print(r, 'this is in the response')
            data = r.json()
            capital = ""
            for cap in data:
                country_capital = cap["capital"][0]
                print(country_capital)
                capital += country_capital
            # print(data)
            message = f'capital of {dic["country"]} is {capital} '
        elif "capital" in dic:
            r = requests.get(url + dic["capital"])
            data = r.json()
            country = ""
            for name in data:
                country_capital = cunt["capital"][0]
                print(country_capital)
                capital += country_capital
            # print(data)
            message = f'capital of {dic["country"]} is {capital} '

        else:
            message = "Select A Country or A Capital"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
