class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk


m1 = Mahasiswa('Satria', '5210411162', 'Informatika', 2021)
m2 = Mahasiswa('Bintang', '521041185', 'Informatika', 2021)
m3 = Mahasiswa('Joshua issac', '5210411189', 'Informatika', 2021)


data_mahasiswa = [m1, m2, m3]

print('Daftar Mahasiswa')
for i in data_mahasiswa:
        print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim}')