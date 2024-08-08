import requests
class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/932eec07ec8ae23f6652"
        response = requests.get(blog_url)
        self.posts=response.json()