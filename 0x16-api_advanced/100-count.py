#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, inst={}, count=0, aft=""):
    """arses the title of all hot articles, and prints a sorted count
    of given keywords."""
    api = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    rlimit = 100
    hdrs = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/dylan_)"
    }
    param = {
        "after": aft,
        "count": count,
        "limit": rlimit
    }
    res = requests.get(api, headers=hdrs, params=param, allow_redirects=False)
    try:
        res_ret = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
       print("")
       return
    res_ret = res_ret.get("data")
    aft = res_ret.get("after")
    count += res_ret.get("dist")
    for child in res_ret.get("children"):
        title = child.get("data").get("title").lower().split()
        for w in word_list:
            if w.lower() in title:
                tlen = len([t for t in title if t == w.lower()])
                if inst.get(w) is None:
                    inst[w] = tlen
                else:
                    inst[w] = inst[w] + tlen
    if aft == None:
        if len(inst) == 0:
            print("")
            return
        inst = sorted(inst.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in inst]
    else:
        count_words(subreddit, word_list, inst, aft, count)
