from collections.abc import Callable
from http.server import BaseHTTPRequestHandler, HTTPServer

import os
from typing import Any

class MyHttpHandlaer(BaseHTTPRequestHandler):


    def do_GET(self):
        print(self.path)
        print('POST')
        self.server.trigger = True
        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.flush()
        
        print('GET')

    def do_POST(self):
        print(self.path)
        print('POST')
        self.server.trigger = True
        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.flush()

class MyHttpServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass: Callable, bind_and_activate: bool = True) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.trigger = False
        self.timeout = 0.000001
        


class ControllServer:
    def __init__(self):
        self.server = MyHttpServer(("127.0.0.1", 5000), MyHttpHandlaer)

    def update(self):
        self.server.handle_request()

    def is_trigger(self):
        return self.server.trigger
    
if __name__ == "__main__":
    server = MyHttpServer(("127.0.0.1", 5000), MyHttpHandlaer)
    server.serve_forever()