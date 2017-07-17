#!/usr/bin/env python3

import socket
from urllib.parse import quote_plus

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\n
Host: maps.google.com:80\n
User-Agent: search4.py\n
Connection: close\n
\n
"""

def geocode(address):
    sock = socket.socket()
    sock.connect(('maps.google.com',80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''

    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more

    print(raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('154 W. End Cir, Verona, WI')
