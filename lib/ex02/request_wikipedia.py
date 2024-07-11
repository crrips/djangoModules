import requests, json, dewiki, sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 request_wikipedia.py <search term>")
        sys.exit(1)
    search_term = sys.argv[1]
    
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        "action": "parse",
        "format": "json",
        "page": search_term,
        "redirects": "true",
        "prop": "wikitext",
    }
    
    response = requests.get(url, params)
    data = json.loads(response.text)
    if data.get("error"):
        print("Error: " + data["error"]["info"])
        sys.exit(1)
        
    filename = search_term.replace(" ", "_")
    f = open(f"{filename}.wiki", "w")
    f.write(dewiki.from_string(data["parse"]["wikitext"]["*"]))
    f.close()
    
    
if __name__ == '__main__':
    main()
    