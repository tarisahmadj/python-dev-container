import os
import requests

def run():
    filename = os.path.basename(__file__)
    print(f"[{filename}] ➡️ Mulai mengeksekusi operasi Requests...")
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    print(f"[{filename}] Mengambil data dari internet (API): {url}")
    
    try:
        # Mengirimkan HTTP GET request
        response = requests.get(url)
        response.raise_for_status() # Cek apakah ada error pada response (misal 404)
        
        # Mengubah hasil response text menjadi format JSON (Dictionary di Python)
        data = response.json()
        print(f"[{filename}] ✅ Data berhasil diambil!")
        print(f"[{filename}] - Task ID : {data.get('id')}")
        print(f"[{filename}] - Judul   : {data.get('title')}")
        print(f"[{filename}] - Status  : {'Selesai' if data.get('completed') else 'Belum Selesai'}")
    except Exception as e:
        print(f"[{filename}] ❌ Gagal mengambil data: {e}")
