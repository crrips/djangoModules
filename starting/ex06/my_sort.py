def ascending(d):
    min_birth_year = min(d.values())

    print("Sorted by birth year:")
    while min_birth_year <= max(d.values()):
        for key, value in d.items():
            if value == min_birth_year:
                print(key)
        min_birth_year = str(int(min_birth_year) + 1)


def alphabetical(d):
    sorted_dict = dict(sorted(d.items()))
    print("\nSorted by last name:")
    for key, value in sorted_dict.items():
        print(key)


if __name__ == '__main__':
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }
    ascending(d)
    alphabetical(d)
