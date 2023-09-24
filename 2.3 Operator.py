'''
Operator, suatu simbol khusus untuk membuat alur logika
Operator dibagi menjadi dua, yaitu;
1. Operator Aritmatika
Operasi aritmatika dasar
- Penjumlahan
langsung penjumlahan
print (1+3)

atau diberikan nilai pada variable terlebih dahulu
a = 3
b = 4
print (a+b)

- Pengurangan
langsung pengurangan
print (1-3)

atau diberikan nilai pada variable terlebih dahulu
a = 3
b = 4
print (a-b)

- Perkalian
langsung perkalian
print (1*3)

atau diberikan nilai pada variable terlebih dahulu
a = 3
b = 4
print (a*b)

- Pembagian
langsung pembagian
print (1/3)

atau diberikan nilai pada variable terlebih dahulu
a = 3
b = 4
print (a/b)
- Modulus (Hasil sisa dari suatu pembagian)
contoh
5 % 3 = 2
langsung dioperasikan
print (1%3)

atau diberikan nilai pada variable terlebih dahulu
a = 4
b = 3
print (a%b)

- Perpangkatan
print(5**2)

atau diberikan nilai pada variable terlebih dahulu
a = 4
b = 3
print (a**b)

2. Operator Perbandingan 
Perbandingan antar dua variable 
- Sama dengan
print(5 == 5)

- Tidak sama dengan
print(5 != 5)

- Lebih besar
print(5 > 5)

- Lebih besar atau sama dengan
print(5 >= 5)

- Lebih kecil
print(5 < 5)

- Lebih kecil atau sama dengan
print(5 <= 5)
'''

A = 5
B = 3

print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A // B) # pembagian bulat kebawah
print(A + B)
print(A ** B)
print(A % B)
print(A == B)
print(A != B)
print(A > B)
print(A >= B)
print(A < B)
print(A <= B)

a = 5
a += 4 # ini sama dengan a = a + 4, hal ini digunakan untuk menyederhanakan suatu codingan
print(a)

a = 5
a *= 4 
print(a)

a = 5
a //= 4 
print(a)


a = 5
a **= 4 
print(a)


a = 5
a %= 4 
print(a)

# aritmatika juga dapat diimplementasikan di pemrogaman, contoh:
a = "Saya sayang ovik"
print (a * 2)

a = True
print(a / 2) # dalam pemrogaman, True dianggap 1 dan False dianggap 0

# Pada operator perbandingan, "is" adalah == dan "is not" adalah !=
a = 5
b = 4

print(a == b)
print(a is b)

print(a != b)
print(a is not b)