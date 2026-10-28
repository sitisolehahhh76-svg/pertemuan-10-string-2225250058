def normalisasi_nama(nama):
    return " ".join(nama.strip().split()).title()

def buat_inisial(nama):
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)

def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)

# Input data dari pengguna
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Proses normalisasi
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
inisial = buat_inisial(nama)
jumlah_kata = len(nama_bersih.split())

# Menampilkan hasil
print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas  : {kode_bersih}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial}")