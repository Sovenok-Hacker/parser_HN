from bs4 import BeautifulSoup
import requests
links = []
x = 0
while True:
    if x == 0:
        url = "https://news.ycombinator.com/newest"
    else:
        url = "https://news.ycombinator.com/" + nlink
    data = requests.get(url).content.decode()
    soup = BeautifulSoup(data, "lxml")
    for link in soup.find_all('a', class_="titlelink"):
        links.append(link.get('href'))
    try: nlink = soup.find('a', class_='morelink').get('href')
    except: break
    x += 1
    for link in links:
        if 'https://github.com' in link: print(link)
