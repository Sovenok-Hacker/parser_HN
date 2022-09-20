import requests
from bs4 import BeautifulSoup

link_end = "newest"

try:
    while True:
        url = f"https://news.ycombinator.com/{link_end}"
        data = requests.get(url).content.decode()
        soup = BeautifulSoup(data, "lxml")
        
        for tag in soup.find_all('a', class_="titlelink"):
            if 'https://github.com' in (link := tag.get('href')):
                print(link)
        try:
            link_end = soup.find('a', class_='morelink').get('href')
        except:
            break
except KeyboardInterrupt:
    pass
