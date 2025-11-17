# ...existing code...
from src.models import Mahasiswa, Dosen, Matakuliah

if __name__ == "__main__":
    mahasiswa = Mahasiswa(user_id=1, username="student1", email="student1@example.com", nim="123456", major="Computer Science")
    dosen = Dosen(user_id=2, username="lecturer1", email="lecturer1@example.com", nip="987654", department="Mathematics")
    matakuliah = Matakuliah(kode="CS101", nama="Introduction to Programming", sks=3)

    print(mahasiswa.get_student_info())
    print(dosen.get_lecturer_info())
    print(matakuliah.get_course_info())
# ...existing code...