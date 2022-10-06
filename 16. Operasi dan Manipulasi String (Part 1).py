# Operasi dan manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "zaskia"
nama_tengah = "adya"
nama_akhir = "mecca"

nama_lengkap = nama_pertama + " " +nama_tengah + " " + nama_akhir
print(nama_lengkap) 

# 2. Menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string

# Mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status)) 

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status)) 

d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status)) 

# Mengulang string
print("ha"*10)
print(10*"ha")

# Indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] : " + nama_lengkap[0:4])
print("index ke-[3:7] : " + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

# Item paling kecil
print("paling kecil : " + min(nama_lengkap))

# Item paling besar
print("paling kecil : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "tasya nur medina"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))