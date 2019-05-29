#!/usr/bin/env python3

from http.server import HTTPServer
from server import Server
import time
import datetime

HOST = 'localhost'
PORT = 8080


def shutdown_server(httpd):
    httpd.shutdown()
    httpd.server_close()
    print(f'{datetime.datetime.now()}: Server DOWN - {HOST}:{PORT}')


if __name__ == '__main__':
    httpd = HTTPServer((HOST, PORT), Server)
    print(f'{datetime.datetime.now()}: Server UP - {HOST}:{PORT}')
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.shutdown()
        print('Keyboard interrupt detected')
        print('Shutting down')
        shutdown_server(httpd)
