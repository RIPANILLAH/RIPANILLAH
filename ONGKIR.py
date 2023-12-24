import os

def hitung_ongkos_kirim():
    ongkos = {'jawa': 9000, 'kalimantan': 10000, 'sumatra': 11000, 'sulawesi': 12000}
    riwayat = []                                                                            # menyimpan riwayat perhitungan dalam bentuk tabel
    
    while True:
        os.system("cls")                                                                    # Membersihkan layar terminal
        
        print(f"{'SELAMAT DATANG DI PROGRAM HITUNG ONGKOS KIRIM':^100}")
        print(f"{'PILIH TUJUAN DAN BERAT BARANG YANG INGIN ANDA KIRIM':^100}")
        print(f"{'-'*100:^100}")

        beban = float(input("Masukkan beban (dalam kg): "))                                 # masukan beban yang ingin di kirim
        tujuan = input("Masukkan tujuan (jawa, kalimantan, sumatra, atau sulawesi): ")      # masukan tujuannya
        
        hasil = beban * ongkos[tujuan]                                                      # Rumus perhitungan awal
        potongan = 0
        if hasil > 1000000:                                                                 # rumus potongan
            potongan = 10000
            hasil -= potongan
        if beban < 20:                                                                      # Rumus diskon
            diskon = 0
        elif 20 <= beban < 40:
            diskon = 0.025
        else:
            diskon = 0.03
        jumlah_diskon = hasil * diskon
        hasil -= jumlah_diskon
        
        riwayat.append([tujuan, beban, jumlah_diskon, potongan, hasil])
        
        os.system("cls")  
        print(f"\n{'Riwayat Perhitungan':^55}")
        print(f"{'-'*55:^55}")
        print("{:<10} {:<10} {:<15} {:<10} {:<10}".format('Tujuan', 'Beban', 'Jumlah Diskon', 'Potongan', 'Hasil'))
        for r in riwayat:
            print("{:<10} {:<10} {:<15} {:<10} {:<10}".format(r[0], r[1], r[2], r[3], r[4]))
        
        lanjut = input("\nApakah anda ingin melakukan perhitungan lagi? (ya/tidak): ")          # looping
        if lanjut.lower() != 'ya':
            break


hitung_ongkos_kirim()
