import requests


class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/571073fbbe7e1fab21be"
        response = requests.get(blog_url)
        self.posts = response.json()
