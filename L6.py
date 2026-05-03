kalimat = input("Masukkan Kalimat: ")

kalimat = kalimat.strip().lower()

print("Awal: ", kalimat[:5])
print("Akhir: ", kalimat[-5:])

tokens = kalimat.split()
print("Token:", tokens)

cari = input("Cari kata: ").lower()
ganti = input("Ganti dengan: ").lower()

hasil = kalimat.replace(cari, ganti)

print("Hasil Akhir", hasil)