import os

def header():
    os.system("cls")

def hasil(message,value):
    print(f"Tujuan ke {message} ongkirnya adalah {value}")

while True:
    header()

    opsi = int(input("1.Pulau Jawa \n2. Pulau Kalimantan \n3. Pulau Sulawesi \n4. Pulau Sumatra \n Masukan pulau yang anda inginkan: "))

    if opsi == 1:
        beratB = int(input("Masukan berat barang anda: "))
        Hberat = beratB * 9000

        if beratB > 20 and beratB <= 40:
            Diskon = Hberat * 0.025
        elif beratB > 40:
            Diskon = Hberat * 0.03
        else:
            Diskon = 0

        if Hberat > 1000000:
            Potongan = Hberat - 10000
        else:
            Potongan = 0
        
        Hakhir = Hberat - Diskon - Potongan 
        hasil("Pulau Jawa",Hakhir)


    elif opsi == 2:
        beratB = int(input("Masukan berat barang anda: "))
        Hberat = beratB * 10000

        if beratB > 20 and beratB <= 40:
            Diskon = Hberat * 0.025
        elif beratB > 40:
            Diskon = Hberat * 0.03
        else:
            Diskon = 0

        if Hberat > 1000000:
            Potongan = Hberat - 10000
        else:
            Potongan = 0
        
        Hakhir = Hberat - Diskon - Potongan
        hasil("Pulau Kalimantan",Hakhir)

    elif opsi == 3:
        beratB = int(input("Masukan berat barang anda: "))
        Hberat = beratB * 11000

        if beratB > 20 and beratB <= 40:
            Diskon = Hberat * 0.025
        elif beratB > 40:
            Diskon = Hberat * 0.03
        else:
            Diskon = 0

        if Hberat > 1000000:
            Potongan = Hberat - 10000
        else:
            Potongan = 0
        
        Hakhir = Hberat - Diskon - Potongan
        hasil("Pulau Sulawesi",Hakhir)

    elif opsi == 4:
        beratB = int(input("Masukan berat barang anda: "))
        Hberat = beratB * 12000

        if beratB > 20 and beratB <= 40:
            Diskon = Hberat * 0.025
        elif beratB > 40:
            Diskon = Hberat * 0.03
        else:
            Diskon = 0

        if Hberat > 1000000:
            Potongan = Hberat - 10000
        else:
            Potongan = 0
        
        Hakhir = Hberat - Diskon - Potongan
        hasil("Pulau Sumatra",Hakhir)

    else:
        print(f"Maaaaf program belum tersedia!!!")

    isContinue = input("Apakah anda ingin Melanjutkan atau Tidak? (Y/N) ")
    if isContinue == "N":
        break

print(f"Program selesai, terima kasih.")
    
    