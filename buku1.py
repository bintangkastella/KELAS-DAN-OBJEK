class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku1 = Buku('Dilan 1991', 'Pidi Baiq', 2015)
buku2 = Buku('Mariposa', 'Hidyatul Fajriyah', 2018)
buku3 = Buku('Life of pi', 'Yann martel', 2001)




toko_buku = [buku1, buku2, buku3, ]

print('Daftar Buku')
for i in toko_buku:
    print(
        f'Buku {i.judul} karangan dari {i.pengarang} pertama kali diterbitkan pada tahun {i.tahun_terbit}')