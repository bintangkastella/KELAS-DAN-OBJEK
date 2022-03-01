class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku = Buku('Life of pi', 'Yann martel', 2001)
print(f'Buku {buku.judul} karangan {buku.pengarang} pertama kali diterbitkan tahun {buku.tahun_terbit}')