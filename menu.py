class menuMinuman:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga


mnm1 = menuMinuman('Cappucino', '+ Banana Cake', 85000)
mnm2 = menuMinuman('Machhiato','+ Strawberry Cake', 80000)
mnm3 = menuMinuman('Cafe latte','+ Tiramisu Cake', 100000)



pilihanMenu = [mnm1, mnm2, mnm3,]
print('Daftar Menu Coffee')

for i in pilihanMenu:
    print('{} harga Rp. {} , {}'.format(i.nama, i.harga, i.deskripsi))