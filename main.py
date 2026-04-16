import uuid

class User:
    def __init__(self, name, role="member"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.role = role
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < 3

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        user = User(data['name'], data['role'])
        user.id = data['id']
        user.borrowed_books = data['borrowed_books']
        return user

    def __str__(self):
        return f"{self.name} ({self.role})"
