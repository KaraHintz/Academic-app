# ...existing code...
from .user import User

class Dosen(User):
    def __init__(self, id, username, email, nip, department):
        super().__init__(id, username, email)
        self.nip = nip
        self.department = department

    def get_lecturer_info(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "nip": self.nip,
            "department": self.department
        }
# ...existing code...