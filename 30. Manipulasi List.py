## Operasi

# index  0 (-3)   1(-2)   2(-1)
data = ["Ucup", "Otong", "Dudung"]

# Mengambil data dari list ini
data_0 = data[0]
print(f"Data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"Data terakhir = {data_terakhir}")

data_ucup = data[-3]
print(f"Data Ucup = {data_ucup}")

# Mengambil info jumlah data dalam list
panjang_data= len(data)
print(f"Panjang data = {panjang_data}")

## Manipulasi data list

# Menambahkan item pada list sesuai posisi
print(f"Data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"Data sesudah ditambahah = \n{data}")

# Menambah di akhir list
data.append("Jajang")
print(f"Data sesudah ditambahah lagi = \n{data}")

# Menambah list dengan list
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"Data gabungan = \n{data}")

# Merubah data
# Kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"Data rubah = \n{data}")

# Meremove data
data.remove("Ujang")
print(f"Data remove = \n{data}")
# data.remove("usep") akan error karena huruf harus sesuai yaitu "Usep"

# Meremove data paling belakang
data_akhir = data.pop()
print(f"Data akhir = \n{data}")
print(data_akhir)