#!/usr/bin/python3
"""
Module for querying the Reddit API recursively and returning a list
containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list containing the titles of hot articles.
        after (str): A token for pagination.

    Returns:
        list: A list containing the titles of hot articles.
               None if the subreddit is not found.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after', None)
        if children:
            for post in children:
                hot_list.append(post.get('data', {}).get('title'))
            if after:
                recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    hot_articles = recurse(subreddit)
    if hot_articles:
        for article in hot_articles:
            print(article)
    else:
        print("None")
