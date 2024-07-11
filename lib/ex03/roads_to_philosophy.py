import sys, requests
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        sys.exit(1)
    article = sys.argv[1]
    url = f"https://en.wikipedia.org/wiki/{article}"
    
    req = requests.get(url)
    if req.status_code != 200:
        print("It's a dead end !")
        sys.exit(1)
    
    soup = BeautifulSoup(req.text, 'html.parser')
    name = soup.find(id="firstHeading").text
    print(name)
    
    names = []
    names.append(name)
    
    counter = 1
    
    while name != "Philosophy":
        content = soup.find(id="mw-content-text")
        paragraphs = content.find_all("p")
        for paragraph in paragraphs:
            if paragraph.find("a", href=True):
                link = paragraph.find("a", href=True)
                if link["href"].startswith("/wiki/"):
                    url = f"https://en.wikipedia.org{link['href']}"
                    break
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        name = soup.find(id="firstHeading").text
        
        print(name)
        
        if name in names:
            print("It leads to an infinite loop !")
            sys.exit(1)
            
        names.append(name)
        counter += 1
        
    print(f"{counter} roads from {sys.argv[1]} to philosophy !")
    
if __name__ == '__main__':
    main()