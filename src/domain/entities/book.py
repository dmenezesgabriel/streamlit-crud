from utils.identifiers import generate_uuid


class Book:
    def __init__(self, id=None, title=None, author=None):
        self.id = id if id else generate_uuid()
        self.title = title
        self.author = author
