# ...existing code...
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def update_user_info(self, username=None, email=None):
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
# ...existing code...