import math
import requests
import argparse

from webserver.database import drone


def your_function():
    longitude = 0
    latitude = 0
    return (longitude, latitude)

def run(current_coords, from_coords, to_coords, SERVER_URL):
    while True:
        drone_coords = your_function()
        with requests.Session() as session:
            drone_location = {'longitude': drone_coords[0],
                              'latitude': drone_coords[1]
                        }
            resp = session.post(SERVER_URL, json=drone_location)
  
   
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    print(current_coords)
    print(from_coords)
    print(to_coords)

    run(current_coords, from_coords, to_coords, SERVER_URL)
