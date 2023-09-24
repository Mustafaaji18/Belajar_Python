'''
While loop, suatu perulangan yang hanya akan dijalankan apabila syarat yang diberikan terpenuhi
perlu diperhatikan bahwa untuk membuat loop ini perlu diberikan kondisi batasan yang memungkinkan loop akan berhenti
jika kondisi yang diberikan terpenuhi, apabila tidak maka program akan looping tanpa batas 

'''
Hadir = 8 #variable
while(Hadir<10): #kondisi loop yang harus dipebuhi
    print("Tingkatkan performa kerjamu", Hadir) #perintah program
    Hadir = Hadir + 1 #syarat kondisi loop, agar loop dapat berhenti

print("Pertahankan kinerjamu !")#opsional jika kondisi syarat yang telah dijalankan sudah tidak terpenuhi

'''
For loop, merupakan suatu perulangan dalam program yang akan berulang sebanyak jumlah perkarakter dalam variable
'''

urutan_hari = [1,2,3,4,5,6] #variable dapat berupa selain list

for x in urutan_hari:
    print('Urutan hari ke ', x)

#jika ingin satu persatu maka sebagai berikut

hari = [1, 2, 3, 4, 5]

for x in hari:
    print('urutan hari ke ...')
    print(x)

# cara pembuatan list dapat menggunakan 2 cara
# cara pertama, manual
lis = [1,2,3,4,5,6]
print(lis)

# cara kedua, otomatis
list_angka = list(range(6))
print(list_angka)

# cara ketiga, memberikan batas awal dan akhir
list_angka_awal = list(range(1, 6)) # ini mengartikan bahwa diawali dengan angka 1 dan diakhiri dengan angka 6
print(list_angka_awal)

# cara keempat
print(list(range(1, 6)))

# cara tersebut dimaksudkan untuk mempermudah coder mempersingkat codingan menjadi lebih ringkas

for x in list(range(1, 9)):
    print('ujian ke ', x)

'''
Nested loop, perulangan ganda atau ada loop dalam loop
'''

i = 90

while (i < 100):
    j = 2
    print((i/j))
    while(j <= (i/j)):
          print('nested loop !')
          i = i+1
          j = j+1

print('Kondisi sudah terpenuhi')

# break and continue
# break, jadi break merupakan suatu program yang akan membuat program berhenti jika menemukan karakter yang telah dideklarasikan
for val in "String":
    if val == "i":
        break
    print(val)

print('Loop telah berakhir !')

# continue merupakan suatu program yang akan membuat program MELEWATI jika menemukan karakter yang telah dideklarasikan
for aku in "String": # jadi variable dapat ditulis sesuai keinginan sama halnya mendeklarasikan varibale pada umumnya
    if aku == "i":
        continue
    print(aku)

print('Loop telah berakhir !')

# cara memadukan for dengan else atau dapat disebut for else
daftar = ['Anggi', 'Roni', 'Denis']
murid  = 'Denis'

for nama in daftar:

    if nama == murid:
        print(nama)
        break
else:
    print('Nama tidak diketahui !')

# jika pada codingan belum selesai dan ingin melanjutkan mengoding maka dapat ditulis "pass" agar tidak error
for nama in daftar:
    pass

if daftar  == 0:
    pass
else:
    pass