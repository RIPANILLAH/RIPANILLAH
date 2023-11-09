# oprasi aritmatika

a = 11
b = 5

print ("====PERTAMBAHAN====")
# oprasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

print ("====PENGURANGAN====")
# oprasi kurang -
hasil = a - b
print(a, '-', b, '=', hasil)

print ("====PERKALIAN====")
# oprasi kali *
hasil = a * b
print(a, '*', b, '=', hasil)

print ("====PEMBAGIAN====")
# oprasi bagi /
hasil = a / b
print(a, '/', b, '=', hasil)

print ("====PANGKAT====")
# oprasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

print ("====SISA PEMBAGIAN====")
# oprasi modulus (sisa pembagian atau persentase) %
hasil = a % b
print(a, '%', b, '=', hasil)

print ("====FLOOR DIVISION====")
# oprasi floor divison (bagi tapi double) //
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas oprasi, oprational preceden
'''
1. ()
2. EXPONEN **
3. PERKALIAN DAN KAWAN-KAWAN % * ** / //
4. PERTAMBAHAN DAN PENGURANGAN + - 
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print (x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil = x ** y * (z + x) / y - y % z // x
print (x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

print ("====TIDAK PAKAI KURUNG====")
hasil = x + y + z
print (x,'+',y,'+',z,'=',hasil )

print ("====PAKAI KURUNG====")
# kurung akan mengambil langkah pertama
hasil = (x + y) * z
print ((x + y),'*',z,'=',hasil )