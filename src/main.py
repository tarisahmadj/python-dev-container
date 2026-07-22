import sys
import os

def main():
    filename = os.path.basename(__file__)
    print(f"[{filename}] 🚀 Memulai program utama...")
    print(f"[{filename}] Menggunakan Python versi: {sys.version.split(' ')[0]}")
    print("-" * 45)
    
    # Eksekusi module_a
    try:
        import module_a
        module_a.run()
    except Exception as e:
        print(f"[{filename}] ⚠️ Error pada module_a: {e}")
    print("-" * 45)
    
    # Eksekusi module_b
    try:
        import module_b
        module_b.run()
    except Exception as e:
        print(f"[{filename}] ⚠️ Error pada module_b: {e}")
    print("-" * 45)
    
    # Eksekusi module_numpy
    try:
        import module_numpy
        module_numpy.run()
    except Exception as e:
        print(f"[{filename}] ⚠️ Error pada module_numpy: {e}")
        print(f"[{filename}] (Tips: Anda mungkin lupa menjalankan 'pip install numpy')")
    print("-" * 45)
    
    # Eksekusi module_requests
    try:
        import module_requests
        module_requests.run()
    except Exception as e:
        print(f"[{filename}] ⚠️ Error pada module_requests: {e}")
        print(f"[{filename}] (Tips: Anda mungkin lupa menjalankan 'pip install requests')")
    print("-" * 45)
    
    print(f"[{filename}] ✅ Semua program telah selesai dijalankan dari main.py!")

if __name__ == "__main__":
    main()
