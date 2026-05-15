jumlah = int(input("Masukkan Jumlah lahan yang telah dipanen; "))

arr = []
for i in range(jumlah):
    data = int(input(f"Masukkan berat panen lahan ke-{i+1}: "))
    arr.append(data)
print(arr)
print("Berat rata-rata: ")
rata= (sum (arr) / jumlah)
print(rata)
