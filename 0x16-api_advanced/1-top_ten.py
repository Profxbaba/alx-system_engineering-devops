#!/usr/bin/python3
"""
Module for querying the Reddit API and printing the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                print(post.get('data', {}).get('title'))
        else:
            print("No hot posts found for the subreddit:", subreddit)
    else:
        print("None")

if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    top_ten(subreddit)
