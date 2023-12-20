import os
os.system("cls")

barang = {"Sabun": 5000, "Shampoo": 10000, "Pasta Gigi": 7000, "Sikat Gigi": 3000, "Tissue": 4000}


def cetak_struk(nama, harga, jumlah, sub, total, bayar, kembali):
    print("Nama Barang   Harga Satuan   Jumlah Barang   Subtotal")
    for i in range(len(nama)):
        print(nama[i],  harga[i],  jumlah[i],  sub[i])
    print("Total", total)
    print("Uang yang dibayar", bayar)
    print("Kembalian", kembali)


nama_barang = []
harga_barang = []
jumlah_barang = []
subtotal = []
total = 0
uang = 0
kembalian = 0


n = int(input("Masukkan jumlah jenis barang yang dibeli: "))


for i in range(n):
    nama = input("Masukkan nama barang ke-" + str(i+1) + ": ")
   
    if nama in barang:
        
        nama_barang.append(nama)
       
        harga = barang[nama]
        harga_barang.append(harga)
        
        jumlah = int(input("Masukkan jumlah barang ke-" + str(i+1) + ": "))
      
        jumlah_barang.append(jumlah)
       
        sub = harga * jumlah
       
        subtotal.append(sub)
        
        total += sub
    else:
        
        print("Barang tidak tersedia, silahkan masukkan lagi!")
        i -= 1


uang = int(input("Masukkan uang yang dibayar: "))


kembalian = uang - total


cetak_struk(nama_barang, harga_barang, jumlah_barang, subtotal, total, uang, kembalian)