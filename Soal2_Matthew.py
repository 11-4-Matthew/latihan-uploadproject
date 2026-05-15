jumlah = int(input("Masukkan jumlah halaman: "))

arr = []
for i in range(jumlah):
    data = int(input(f"Masukkan halaman ke-{i+1}: "))
    arr.append(data)
print("List halaman sekarang adalah: ")
print(arr)

print("1. hapus data")
print("2. edit data")
print("3. tambah data")
print("4. Lihat data sekarang")
print("5. analisa")

pilihan = int(input("pilihan (nomer):"))
if pilihan == 1:
    hapus = int(input("Masukkan data yang ingin dihapus: "))
    if hapus in arr:
        arr.remove(hapus)
        print(arr)
    else:
        print("Masukkan data yang valid")

 
elif pilihan == 2:
    hal_edit= int(input("urutan data yang ingin di edit: "))
    if 1<= hal_edit <= len(arr):
        edit = input(f"Masukkan data yang baru untuk urutan ke-{hal_edit}: ")
        arr[hal_edit - 1] = edit
        print(arr)
    else:
        print("Urutan tidak valid")

elif pilihan == 3:
    tambah = int(input("Masukkan data yang ingin ditambahkan: "))
    arr.append(tambah)
    print(arr)
    
elif pilihan == 4:
    print(arr)

else:
    print("rata-rata halaman:")
    print(sum(arr)/jumlah)

    