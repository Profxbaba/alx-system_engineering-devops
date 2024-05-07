#!/usr/bin/python3
"""
Module for counting occurrences of given keywords in hot articles of a subreddit.
"""

import requests

def count_words(subreddit, word_list, hot_list=None, after=None):
    """
    Queries the Reddit API recursively and counts occurrences of given keywords
    in the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list containing the keywords to count occurrences of.
        hot_list (list): A list containing the titles of hot articles.
        after (str): A token for pagination.

    Returns:
        dict: A dictionary containing the counts of each keyword.
    """
    if hot_list is None:
        hot_list = []

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
                count_words(subreddit, word_list, hot_list, after)
        return count_occurrences(hot_list, word_list)
    else:
        return None

def count_occurrences(hot_list, word_list):
    """
    Counts occurrences of given keywords in the titles of hot articles.

    Args:
        hot_list (list): A list containing the titles of hot articles.
        word_list (list): A list containing the keywords to count occurrences of.

    Returns:
        dict: A dictionary containing the counts of each keyword.
    """
    word_count = {}
    for word in word_list:
        count = sum(1 for title in hot_list if ' ' + word.lower() + ' ' in title.lower())
        if count > 0:
            word_count[word.lower()] = count
    return word_count

if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    word_list = input("Enter the keywords separated by spaces: ").split()
    keyword_counts = count_words(subreddit, word_list)
    if keyword_counts:
        sorted_counts = sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print("{}: {}".format(keyword, count))
