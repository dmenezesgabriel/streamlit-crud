from utils.identifiers import generate_uuid


class Author:
    def __init__(self, id=None, name=None):
        self.id = id if id else generate_uuid()
        self.name = name
