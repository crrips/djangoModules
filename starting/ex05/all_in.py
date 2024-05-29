import sys


def ft_city(states: dict, capital_cities: dict, city: str):
    for state in states:
        if city == capital_cities[states[state]]:
            print(f"{city} is the capital of {state}")


def ft_state(states: dict, capital_cities: dict, state: str):
    for city in capital_cities:
        if city == states[state]:
            print(f"{capital_cities[city]} is the capital of {state}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        prompt = sys.argv[1]
    else:
        sys.exit(1)

    split = prompt.split(",")
    for i in range(len(split)):
        split[i] = split[i].strip()

    for i in split:
        if i == '':
            split.remove(i)

    after = []
    for i in split:
        if i and i not in after:
            after.append(i)

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

    for i in after:
        if i.title() in states:
            ft_state(states, capital_cities, i.title())
        elif i.title() in capital_cities.values():
            ft_city(states, capital_cities, i.title())
        else:
            print(f"{i} is neither a capital city nor a state")
            