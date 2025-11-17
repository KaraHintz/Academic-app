# ...existing code...
from .user import User

class Mahasiswa(User):
    def __init__(self, id, username, email, nim, major):
        super().__init__(id, username, email)
        self.nim = nim
        self.major = major

    def get_student_info(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "nim": self.nim,
            "major": self.major
        }
# ...existing code...