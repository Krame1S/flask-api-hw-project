from model.user import User


class BlogPost:

    def __init__(self, body: str, author: User):
        self.body = body
        self.author = author 