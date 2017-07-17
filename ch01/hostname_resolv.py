#!/usr/bin/env python3

import socket

if __name__ == '__main__':
    hostname = 'ravel.home.jaxon.io'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))
