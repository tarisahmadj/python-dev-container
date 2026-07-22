import os
# pyrefly: ignore [missing-import]
import numpy as np

def run():
    filename = os.path.basename(__file__)
    print(f"[{filename}] ➡️ Mulai mengeksekusi operasi Numpy...")
    
    # Membuat array/matriks 3x3
    matrix = np.array([
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ])
    print(f"[{filename}] Matriks 3x3:")
    print(matrix)
    
    # Melakukan beberapa perhitungan dasar Numpy
    total_sum = np.sum(matrix)
    rata_rata = np.mean(matrix)
    
    print(f"[{filename}] Total jumlah semua elemen: {total_sum}")
    print(f"[{filename}] Nilai rata-rata elemen: {rata_rata}")
