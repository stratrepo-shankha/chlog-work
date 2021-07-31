import requests
from bs4 import BeautifulSoup
import json


class NewsScraper:
    def __init__(self, link) -> None:
        self.link = link

    def returnsoupobj(self) -> BeautifulSoup:
        link = self.link
        try:
            r = requests.get(link)
            return BeautifulSoup(r.content, 'html.parser')
        except:
            Exception('Bad Link')

    def getresult(self, intermediate: list, final: dict) -> list:
        self.soup = self.returnsoupobj()
        for element in intermediate:
            if element['type'] == 'id':
                self.soup = self.soup.find(element['name'], id=element['key'])
            elif element['type'] == 'class':
                self.soup = self.soup.find(
                    element['name'], class_=element['key'])
            else:
                raise TypeError('Can be of type id or class')

        if final['type'] == 'id':
            self.soup = self.soup.find_all(final['name'], id=final['key'])
        elif final['type'] == 'class':
            self.soup = self.soup.find_all(final['name'], class_=final['key'])
        elif final['type'] == 'attrs':
            self.soup = self.soup.find_all(final['name'], attrs=final['key'])
        else:
            raise TypeError('Can be of type id or class')

        return self.soup

    def getlinks(self, baselink: str, souplist: list) -> list:
        try:
            newslinks = []

            for _ in range(len(souplist)):
                newslinks.append(baselink + souplist[_].a['href'])

            return newslinks
        except:
            Exception('Bad Structure Provided')

    def tojson(self, souplist: list) -> json:
        self.individual = []

        for _ in range(len(souplist)):
            self.individual.append(
                souplist[_].get_text().encode("ascii", "ignore").decode())

        return json.dumps(self.individual)
