# check the website you wish to scrape for a robots.txt, this will tell you which pages are allowed to scrape.

import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['score'], reverse=True)


def create_custom_hacker_news(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = mega_subtext[index].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hn.append({'title': title, 'link': href, 'score': score})
    return sort_stories_by_votes(hn)



resp = requests.get('https://news.ycombinator.com/news')
resp2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(resp.text, 'html.parser')
soup2 = BeautifulSoup(resp2.text, 'html.parser')
links = soup.select('.storylink') # .score will work on classes #score will grab the id tags
links2 = soup2.select('.storylink') # .score will work on classes #score will grab the id tags
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
mega_link = links + links2
mega_subtext = subtext + subtext2




pprint.pprint(create_custom_hacker_news(mega_link, mega_subtext))




