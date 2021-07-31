from chlogscraper import *

# Examples


# News
baselink = 'https://www.reuters.com/business'
websitelink = 'https://www.reuters.com'

ns = NewsScraper(link=baselink)

intermediate = []

final = {
    'name': 'div',
    'type': 'attrs',
    'key': {'class': lambda e: e.startswith('StoryCollection') if e else False},
}


soup = ns.getresult(intermediate=intermediate, final=final)
links = ns.getlinks(baselink=websitelink, souplist=soup)

print(links)


# Twitter
apikey = ""
apisecretkey = ""
accesstoken = ""
accesstokensecret = ""


tw = TwitterAPI(apikey, apisecretkey, accesstoken, accesstokensecret)

statuses = tw.timelinesearch(key='Tacs_gg')

print(statuses)