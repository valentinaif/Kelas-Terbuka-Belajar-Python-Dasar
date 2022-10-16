# Break


print("\n=====CONTOH 1=====\n")

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3 :
        print("Nice bro!")
        break
    print("Okey")
print("cukup sudah")

print("\n=====CONTOH 2=====\n")

data_int =int(input("Hitung sampai = "))

angka = 0

while True :
    angka += 1
    print(f"count = {angka}")

    if angka == data_int :
        print("Nice bro!")
        break
    print("Okey")
print("cukup sudah")