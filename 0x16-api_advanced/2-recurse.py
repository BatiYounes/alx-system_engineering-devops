#!/usr/bin/python3
"""Module hat queries the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns a list containing the titles of all hot articles for
    a given subreddit, None if no result are found."""
    apiurl = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/lapbox_)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(apiurl, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")

    for re in res.get("children"):
        hot_list.append(re.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
