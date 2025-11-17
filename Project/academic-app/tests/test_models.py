import unittest
from src.models.user import User
from src.models.mahasiswa import Mahasiswa
from src.models.dosen import Dosen
from src.models.matakuliah import Matakuliah

class TestModels(unittest.TestCase):

    def test_user_creation(self):
        user = User(id=1, username='testuser', email='test@example.com')
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_mahasiswa_creation(self):
        mahasiswa = Mahasiswa(id=2, username='studentuser', email='student@example.com', nim='123456', major='Computer Science')
        self.assertEqual(mahasiswa.id, 2)
        self.assertEqual(mahasiswa.username, 'studentuser')
        self.assertEqual(mahasiswa.email, 'student@example.com')
        self.assertEqual(mahasiswa.nim, '123456')
        self.assertEqual(mahasiswa.major, 'Computer Science')

    def test_dosen_creation(self):
        dosen = Dosen(id=3, username='lectureruser', email='lecturer@example.com', nip='789012', department='Mathematics')
        self.assertEqual(dosen.id, 3)
        self.assertEqual(dosen.username, 'lectureruser')
        self.assertEqual(dosen.email, 'lecturer@example.com')
        self.assertEqual(dosen.nip, '789012')
        self.assertEqual(dosen.department, 'Mathematics')

    def test_matakuliah_creation(self):
        matakuliah = Matakuliah(kode='CS101', nama='Introduction to Computer Science', sks=3)
        self.assertEqual(matakuliah.kode, 'CS101')
        self.assertEqual(matakuliah.nama, 'Introduction to Computer Science')
        self.assertEqual(matakuliah.sks, 3)

if __name__ == '__main__':
    unittest.main()