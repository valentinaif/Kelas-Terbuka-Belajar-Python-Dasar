# Latihan Perulangan membuat Segitiga

sisi = 10

# 1. Menggunakan for

# dummy variable
print("Awal dari for")
count = 1
for i in range(sisi) :
    print("*"*count)
    count += 1
print("Akhir dari for\n")


# 2. Menggunakan while

print("Awal dari while")
count = 1
while True :
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("Akhir dari while")

# 3. Hanya ganjil saja

print("Awal dari while")
count = 1
while True :
    if count%2:
        # akan print jika ganjil
        print("*"*count)
        count += 1
    else :
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("Akhir dari while")

# 4. Hanya ganjil saja

print("Awal dari while")
count = 1
spasi = int(sisi/2)
while True :
    if count%2:
        # akan print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else :
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("Akhir dari while")