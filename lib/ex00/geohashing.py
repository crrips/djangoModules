import sys
import antigravity


def main():
    if len(sys.argv) == 3:
        try:
            latitude = float(sys.argv[1])
            longitude = float(sys.argv[2])
            datedow = sys.argv[0].encode("utf-8")
            antigravity.geohash(latitude, longitude, datedow)
        except ValueError:
            print("Input must be a float number")
    else:
        print("Usage: python3 geohashing.py <latitude> <longitude>")


if __name__ == '__main__':
    main()