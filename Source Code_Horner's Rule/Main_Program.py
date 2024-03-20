#Created By Yudi Mubarok
#NIM : 22343081
#PROGRAM ALGORITMA HORNER'S RULE

def HORNER_EVALUASI_POLINOM(polinom, x):
    # Memeriksa apakah polinom tidak kosong dan x adalah angka
    if len(polinom) == 0 or not isinstance(x, (int, float)):
        print("Error: Polinom kosong atau x bukan angka")
        return None
    
    # Menentukan pangkat tertinggi dari polinom
    pangkat = len(polinom) - 1
    
    # Inisialisasi variabel hasil dengan koefisien tertinggi
    hasil = polinom[pangkat]

    # Mencetak informasi awal
    print("Evaluasi polinom:")
    print("Polinom:", polinom)
    print("Nilai x:", x)
    print("Pangkat tertinggi polinom:", pangkat)
    
    # Iterasi dari koefisien tertinggi hingga koefisien konstanta
    for i in range(pangkat - 1, -1, -1):
        # Memeriksa apakah nilai hasil melebihi batas atas tipe data yang diizinkan
        if hasil > float('inf'):
            print("Error: Hasil evaluasi melebihi batas atas tipe data yang diizinkan")
            return None
        
        # Menghitung hasil evaluasi dengan menggunakan rumus Horner's Rule
        hasil = hasil * x + polinom[i]

        # Mencetak informasi setiap langkah evaluasi
        print("Langkah", pangkat - i, ":")
        print("    Koefisien:", polinom[i])
        print("    Nilai x:", x)
        print("    Hasil sementara:", hasil)
    
    # Mencetak hasil evaluasi akhir
    print("Hasil evaluasi polinom pada x =", x, "adalah", hasil)

    return hasil

# Contoh penggunaan
polinom = [2, -3, 1]  # Contoh: 2x^2 - 3x + 1
x = 2
HORNER_EVALUASI_POLINOM(polinom, x)
