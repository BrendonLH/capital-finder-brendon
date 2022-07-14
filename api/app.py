from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        print(url_components)
        dic = dict(query_string_list)
        print(dic)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            print(r, 'this is in the response')
            country = r.json()
            capital = []
            for cap in country:
                country_capital = cap["capital"][0]
                print(country_capital)
                capital.append(country_capital)
            # print(data)
            message = str(capital)

        else:
            message = "Select A Country or A Capital"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
