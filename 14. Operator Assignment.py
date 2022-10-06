#Operasi yang dapat dilakukan dengan penyingkatan
#Operasi ditambah dengan assigment

a = 5 # adalah assigment
print("nilai a =", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi = ", a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi = ", a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi = ", a)

a /= 2 # artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi = ", a)

b = 10
print("\nnilai b =",b)

#Modulus dan Floor Division
b %= 3 # artinya adalah b = b % 3
print("nilai b %= 3, nilai b menjadi = ", b)

b = 10
print("\nnilai b =",b)

b //= 3 # artinya adalah b = b // 3
print("nilai b //= 3, nilai b menjadi = ", b)

#Pangkat atau Eksponen
a = 5
print("nilai a = ",a)
a **= 3
print("nilai a **= 3, nilai a menjadi = ", a)


#Operasi Bitwise
#OR
c = True
print("\nnilai c = ", c)
c |= False
print("nilai c |= False, nilai c menjadi = ",c)
c = False
print("nilai c = ", c)
c |= False
print("nilai c |= False, nilai c menjadi = ",c)

#AND
c = True
print("\nnilai c = ", c)
c &= False
print("nilai c &= False, nilai c menjadi = ",c)
c = True
print("nilai c = ", c)
c &= True
print("nilai c &= False, nilai c menjadi = ",c)

#XOR
c = True
print("\nnilai c = ", c)
c ^= False
print("nilai c ^= False, nilai c menjadi = ",c)
c = True
print("nilai c = ", c)
c ^= True
print("nilai c ^= False, nilai c menjadi = ",c)

#Geser Geser
d = 0b0100
print("\nnilai d = ", format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi = ", format(d, '04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi = ", format(d, '04b'))