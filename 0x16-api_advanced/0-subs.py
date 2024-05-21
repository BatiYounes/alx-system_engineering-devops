#!/usr/bin/python3
"""unction that queries the Reddit API and returns the number
of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers not active users but all
    subscribers, if an invalide subreddit is given return 0."""
    api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/usr_)"
    }

    res = requests.get(api, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0

    res_returned = res.json().get('data')

    return res_returned.get('subscribers')
