#!/usr/bin/python3
'''
returns number of subscribers for a given subreddit
'''
import requests


def number_of_subscribers(subreddit):
    """ show the numbers of sub """
    user_agent = {'User-agent': 'jboat1'}
    sub = requests.get('http://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user_agent)
    try:
        sub = sub.json().get('data')
        for k, v in sub.items():
            if k == 'subscribers':
                return(v)
    except BaseException:
        return(0)
