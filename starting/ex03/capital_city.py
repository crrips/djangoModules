import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        state = sys.argv[1]
    else:
        print("Error: invalid number of arguments")
        sys.exit(1)

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }

    if not state in states:
        print("Unknown state")
        sys.exit(0)

    for city in capital_cities:
        if city == states[state]:
            print(capital_cities[city])
            sys.exit(0)
