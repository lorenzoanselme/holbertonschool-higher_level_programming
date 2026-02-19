#!/usr/bin/python3
"""
Module that fetches posts from a RESTful API and either prints their titles
or saves them to a CSV file.
"""
import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches posts from the API and prints their titles.
    If the request fails, it prints "Status Code: None".
    """
    response = requests.get(URL)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from the API and saves them to a CSV file.
    If the request fails, it prints "Status Code: None".
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()
        
        data =[]
        for post in posts:
            data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("post.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, filenames=["id", "title", "body"])
            writer.writeheader()
            writer.writerow(data)
