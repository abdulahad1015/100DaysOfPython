import requests
class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
        response = requests.get(blog_url)
        self.posts=response.json()