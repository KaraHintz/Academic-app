# ...existing code...
class Matakuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def get_course_info(self):
        return {
            "kode": self.kode,
            "nama": self.nama,
            "sks": self.sks
        }