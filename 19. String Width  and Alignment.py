# Width and Multiline

# Data

data_nama = "Ucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# String
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"=" + "Data String" + 5 * "=")
print(data_string)

# String Multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"=" + "Data String" + 5 * "=")
print(data_string)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + "Data String" + 5 * "=")
print(data_string)

# String Multiline (kutip triplet)
data_string = f"""
nama         = {data_nama:>5}
umur         = {data_umur:>5}
tinggi       = {data_tinggi:>5}
nomor sepatu = {data_nomor_sepatu:>5}
"""
print("\n" + 5*"=" + "Data String" + 5 * "=")
print(data_string)

#