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
apikey = "OyRMxGm5p34dTwNQaWveZn1GS"
apisecretkey = "85h3T3Ttu9KWUQtzP2wTnSWwcyxnAJZHQmuynEKPAJ7qVZWx4R"
accesstoken = "393345191-mDSlC24MeEauVI0vthNjQzXBlvupJUNjYxPeQYoL"
accesstokensecret = "0n8IGlHv0VuzT0DnZOtkeOmftWoeHhlZtFmzIBFkkqNAa"


tw = TwitterAPI(apikey, apisecretkey, accesstoken, accesstokensecret)

statuses = tw.timelinesearch(key='Tacs_gg')

print(statuses)