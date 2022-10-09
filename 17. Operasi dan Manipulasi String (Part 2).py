# Operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case
salam = "sist!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeRen AbieZZZzzzZZZz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "bro"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semua huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline |n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okey Not To Be Okey"
cek_judul = judul.istitle() # hasil bool

print(judul + " is title = " + str(cek_judul))

## mengecek komponen startswith() endswith() <-- keren
cek_start = "Wooshik Oppa".startswith("Wooshik")
print("start = " + str(cek_start))

cek_end = "Wooshik Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## Penggabungan komponen join() split()

pisah = ["aku", "rindu", "kamu"]
gabungan = ",".join(pisah)
print(pisah)
print(gabungan)

gabungan = " ".join(pisah)
print(pisah)
print(gabungan)

gabungan = " ehm ".join(pisah)
print(gabungan)

gabungan = "akuehmrinduehmkamu"
print(gabungan.split("ehm"))

## alokasi karakter rjust(), ljust(), center()

print(5*"=" + "data" + "="*5)

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, ":")
print("'" + tengah + "'")

# kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'" + tengah + "'")

kiri = "kiri".strip(" ")
print("'" + kiri + "'")

kanan = "kanan".strip(" ")
print("'" + kanan + "'")
