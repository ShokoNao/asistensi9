# main.py

from service import JadwalDokter
from ui import Menu

if __name__ == "__main__":
    # 1. Buat instance dari service (logika bisnis)
    jadwal_dokter_service = JadwalDokter()
    
    # 2. Buat instance dari UI dan berikan akses ke service
    menu_ui = Menu(jadwal_dokter_service)
    
    # 3. Jalankan menu utama dari UI
    menu_ui.tampilkan_menu()