#Latihan Konversi Temperatur

#Program konversi celcius ke satuan lain

print("\nProgram Konversi Temperatur\n")

celcius = float(input("Masukan suhu dalam celcius = "))
print("suhu adalah", celcius, "celcius")

#Reamur
reamur = (4/5)*celcius
print("suhu dalam reamur adalah", reamur, "reamur")

#Fahrenheit
fahrenheit = (9/5)*celcius+32
print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

#Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "kelvin")