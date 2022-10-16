# Continue, Pass

# Pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

#angka = 0

#while angka < 5:
#    angka += 1
#    if angka == 3:
#        pass # ini tidak akan dieksekusi
#    print(angka)

#Continue

angka = 0
print(f"Angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}") # aksi 1
   
    if angka == 3 :
        print("Nice!")    
        continue # akan membuat loop meloncat ke step selanjutnya
    print("hai") # aksi 2

print("Finish")