#!/usr/bin/python3
"""module that queries the Reddit API."""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given
    subreddit."""
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/lapbox_)"
    }

    params = {
        "limit": 10
    }

    res = requests.get(api_url, headers=headers, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return

    res_returned = res.json().get("data")

    [print(r.get("data").get("title")) for r in res_returned.get("children")]
