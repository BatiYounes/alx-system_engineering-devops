#!/usr/bin/python3
# This script defines a function that returns the number of subscribers for a
# given subreddit.

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-user-agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
