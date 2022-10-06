#Operasi Aritmatika

a = 10
b = 3

#Operasi tambah "+"
hasil = a + b
print(a,"+",b,"=",hasil)

#Operasi pengurang "-"
hasil = a - b
print(a,"-",b,"=",hasil)

#Operasi perkalian "*"
hasil = a * b
print(a,"*",b,"=",hasil)

#Operasi pembagian "/"
hasil = a / b
print(a,"/",b,"=",hasil)

#Operasi eksponen (pangkat) "**"
hasil = a ** b
print(a,"**",b,"=",hasil)

#Operasi modulus "%"
hasil = a % b
print(a,"%",b,"=",hasil)

#Operasi floor devision "//"
hasil = a // b
print(a,"//",b,"=", hasil)

#Prioritas operasi (), eksponen, perkalian pembagian mod floor div, penambahan pengurangan 

x = 3
y = 2
z = 4
hasil  = x ** y * z + x / y - y % z // x
print (x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil)

#kurang mengambil langkah paling pertama
hasil = (x + y) * z
print((x, "+", y), "*", z, "=", hasil)