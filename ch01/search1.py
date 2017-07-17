#!/usr/bin/env python3

from pygeocoder import Geocoder

if  __name__ == '__main__':
    address = '154 W. End Cir, Verona, WI'
    print(Geocoder.geocode(address)[0].coordinates)
    print('Good? Idk.')
