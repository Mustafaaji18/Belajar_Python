'''
Condition, suatu keadaan yang akan dijalankan jika memenuhi suatu persyaratan
Condition sendiri dibagi menjadi tiga, yaitu
1. if (digunakan hanya jika memenuhi satu persyaratan, maka program akan menjalankan perintah. jika tidak maka tidak akan dijalankan)
2. if - else (suatu kondisi yang memiliki satu persyaratan yang harus dipenuhi, jika tidak akan dialihkan untuk menjalankan perintah lain)
3. if - elif - else (kondisi yang memiliki multi persyaratan / banyak opsi persyaratan, sehingga jika tidak ada yang sesuai kondisi maka
   akan dialihkan kepada opsi terakhir yaitu else)

ketiga kondisi tersebut hanya membedakan tingkat kompleksitas persyaratan yang harus dipenuhi untuk menjalankan suatu perintah
'''
# 1. Fungsi if
absen = 1

if absen <= 2:
    print("Gaji dipotong 35%")

# 2. Fungsi if - else
Masuk = 24

if Masuk <= 25:
    print("Perbaiki semangat kerjanya !")

else:
    print("Selamat anda menjadi pegawai teladan !")

# 3. Fungsi if - elif - else
ijin = 5

if ijin == 3:
    print("Jaga kesehatan ya !")

elif ijin <= 3:
    print("Pertahankan kebugaran badan ya !")

else:
    print("Coba refleksi diri, mungkin anda kurang motivasi !")

# Jika fungsi if elif else memiliki elif lebih dari 1

score = 62

if score >= 85:
    print("Predikat A / Sangat Memuaskan")

elif score >= 75:
    print("predikat B / Memuaskan")

elif score >= 70:
    print("Predikat B- / Cukup Memuaskan")

elif score >= 65:
    print("Predikat C / Cukup Memuaskan")

elif score >= 60:
    print("Predikat C- / Kurang Memuaskan")

else:
    print("predikat D / Kurang Memuaskan")

# Jika terdapat fungsi if dalam fungsi if
kelas = 1
score = 65

if kelas > 1:
    if score >= 85:
        print("predikat A / Sangat Memuaskan (Lulus)")

    elif score >= 75:
        print("Predikat B / Cukup Memuaskan (Lulus)")

    elif score >= 70:
        print("Predikat C / Memuaskan (Lulus)")
    else:
        print("Predikat D / Kurang Memuaskan (Tidak Lulus)")

else:
    if score >= 65:
        print("Lulus")
    else:
        print("Tidak Lulus")

# Cara memasukkan angka oleh user
Passing = float(input("Nilai passing grade ujian rating: ")) 
# gunakan tipe data float sehingga jika ditulis angka desimal maka tidak error

if Passing >= 70:
    print("Lulus")

else:
    print("Tidak Lulus, lakukan uji kompetensi kembali")