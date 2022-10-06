data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara Membuat String

'''
	1. dengan menggunakan single quote '...'
	2. dengan menggunakan double quote "...."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar"')
print("'Halo, apa kabar'")
print("Inu adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\t\totong, jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") #LF => line feed _ unix, macos, linux
print("baris pertama.\rbaris kedua.") #CR => carriage return _ commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF => line feed carriage return _ windows

# 3. String Literal atau raw

# hati-hati
print("C:\new folder") # akan salah pathnya

# menggunakan raw string
print(r"C:\new folder")

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan raw
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
""")