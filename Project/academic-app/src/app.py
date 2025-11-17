from flask import Flask, render_template
from src.models import Mahasiswa, Dosen, Matakuliah

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    mahasiswa = Mahasiswa(id=1, username="student1", email="student1@example.com", nim="123456", major="Computer Science")
    dosen = Dosen(id=2, username="lecturer1", email="lecturer1@example.com", nip="987654", department="Mathematics")
    matakuliah = Matakuliah(kode="CS101", nama="Introduction to Programming", sks=3)
    return render_template("index.html", mahasiswa=mahasiswa, dosen=dosen, matakuliah=matakuliah)


if __name__ == "__main__":
    app.run(debug=True)
