import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        city = sys.argv[1]
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

    for state in states:
        if city == capital_cities[states[state]]:
            print(state)
            sys.exit(0)

    print("Unknown capital city")
    sys.exit(0)
