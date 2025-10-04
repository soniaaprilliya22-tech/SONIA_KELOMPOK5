# non return function 
def non_return_function(nama, nim):
  print("Selamat datang di praktikum Pemrograman Dasar 2025 {} dengan NIM {}".format(nama, nim))


# return function 
def return_func(angka):
  print(f"Angka kalian adalah {angka}")
  if angka % 2 == 0:
    return print("Mengembalikan nilai genap dengan angka {}".format(angka))
  else:
    return print("Mengembalikan nilai ganjil dengan angka {}".format(angka))


# arbitrary function 
def arbitrary_func(*penutup):
  for nama in penutup:
    print(f"Terima kasih {nama}")


# anonymous function 
add = lambda x, y: x + y
result = add(5, 8)

# Menjalan fungsi 
non_return_function("Sonia", 21120125120020)
return_func(13)
arbitrary_func("- Coba 1", "- Coba 2", "- Coba 3")
print(add(4, 9))