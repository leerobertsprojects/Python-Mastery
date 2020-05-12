# check the website you wish to scrape for a robots.txt, this will tell you which pages are allowed to scrape.

import requests
from bs4 import BeautifulSoup
import pprint

resp = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(resp.text, 'html.parser')

links = soup.select('.storylink') # .score will work on classes #score will grab the id tags
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['score'], reverse=True)


def create_custom_hacker_news(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hn.append({'title': title, 'link': href, 'score': score})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hacker_news(links, subtext))


