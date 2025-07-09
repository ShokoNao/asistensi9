# ui.py

class Menu:
    """Kelas untuk antarmuka pengguna (Presentation/UI Layer)"""
    def __init__(self, jadwal_dokter_service):
        self.service = jadwal_dokter_service
    
    def _print_dokter_details(self, dokter, show_hari=True):
        """Fungsi bantuan untuk mencetak detail dokter"""
        print(f"Nama Dokter: {dokter.nama}")
        print(f"Spesialis: {dokter.spesialis}")
        if show_hari:
            print(f"Hari: {', '.join(dokter.hari)}")
        print(f"Jam: {dokter.jam}\n")

    def tampilkan_semua_jadwal(self):
        print("\n=== Semua Jadwal Dokter ===")
        all_dokters = self.service.get_all_schedules()
        if not all_dokters:
            print("Tidak ada jadwal dokter yang tersedia.")
            return
        for dokter in all_dokters:
            self._print_dokter_details(dokter)
            
    def tampilkan_jadwal_berdasarkan_abjad(self):
        print("\n=== Jadwal Dokter Berdasarkan Abjad ===")
        sorted_dokters = self.service.get_schedules_sorted_by_name()
        if not sorted_dokters:
            print("Tidak ada jadwal dokter yang tersedia.")
            return
        for dokter in sorted_dokters:
            self._print_dokter_details(dokter)

    def tampilkan_jadwal_berdasarkan_urutan_hari(self):
        print("\n=== Jadwal Dokter Berdasarkan Urutan Hari ===")
        jadwal_per_hari = self.service.get_schedules_grouped_by_day()
        jadwal_ditemukan_global = False
        for hari, dokters in jadwal_per_hari.items():
            if dokters:
                jadwal_ditemukan_global = True
                print(f"\n--- HARI {hari.upper()} ---")
                for dokter in dokters:
                    self._print_dokter_details(dokter, show_hari=False)
        if not jadwal_ditemukan_global:
            print("Tidak ada jadwal dokter yang tersedia.")

    def cari_jadwal_berdasarkan_spesialis(self):
        spesialis = input("Masukkan spesialisasi yang dicari: ")
        results = self.service.find_by_specialist(spesialis)
        print("\n--- Hasil Pencarian ---")
        if not results:
            print("Spesialis tidak ditemukan.")
        else:
            for dokter in results:
                self._print_dokter_details(dokter)

    def cari_jadwal_berdasarkan_hari(self):
        hari = input("Masukkan hari yang dicari (e.g., Senin): ")
        results = self.service.find_by_day(hari)
        print("\n--- Hasil Pencarian ---")
        if not results:
            print("Tidak ada jadwal pada hari tersebut.")
        else:
            for dokter in results:
                self._print_dokter_details(dokter)

    def cari_jadwal_berdasarkan_nama(self):
        nama = input("Masukkan nama dokter yang dicari: ")
        results = self.service.find_by_name(nama)
        print("\n--- Hasil Pencarian ---")
        if not results:
            print("Dokter tidak ditemukan.")
        else:
            for dokter in results:
                self._print_dokter_details(dokter)

    def tambah_dokter(self):
        print("\n--- Tambah Dokter Baru ---")
        nama = input("Masukkan nama dokter: ")
        spesialis = input("Masukkan spesialisasi: ")
        hari = input("Masukkan hari praktek (pisahkan dengan koma, contoh: Senin,Rabu): ")
        jam = input("Masukkan jam praktek (contoh: 09:00 - 12:00): ")
        self.service.add_doctor(nama, spesialis, hari, jam)
        print("Dokter berhasil ditambahkan.")

    def hapus_dokter(self):
        nama = input("Masukkan nama dokter yang ingin dihapus: ")
        if self.service.remove_doctor(nama):
            print(f"Dokter {nama} berhasil dihapus.")
        else:
            print(f"Dokter dengan nama {nama} tidak ditemukan.")

    def tampilkan_menu(self):
        """Menampilkan menu interaktif"""
        actions = {
            '1': self.tampilkan_semua_jadwal,
            '2': self.cari_jadwal_berdasarkan_spesialis,
            '3': self.cari_jadwal_berdasarkan_hari,
            '4': self.cari_jadwal_berdasarkan_nama,
            '5': self.tambah_dokter,
            '6': self.hapus_dokter,
            '7': self.tampilkan_jadwal_berdasarkan_abjad,
            '8': self.tampilkan_jadwal_berdasarkan_urutan_hari,
        }
        while True:
            print("\n=== Menu Utama ===")
            print("1. Tampilkan Semua Jadwal")
            print("2. Cari Jadwal Berdasarkan Spesialis")
            print("3. Cari Jadwal Berdasarkan Hari")
            print("4. Cari Jadwal Berdasarkan Nama Dokter")
            print("5. Tambah Dokter")
            print("6. Hapus Dokter")
            print("7. Tampilkan Semua Jadwal (Urut Abjad)")
            print("8. Tampilkan Semua Jadwal (Urut Hari)")
            print("9. Keluar")
            pilihan = input("Pilih menu [1-9]: ")

            if pilihan == '9':
                print("Terima kasih telah menggunakan program jadwal dokter! 👋")
                break
            
            action = actions.get(pilihan)
            if action:
                action()
            else:
                print("Pilihan tidak valid. Silakan masukkan angka dari 1 hingga 9.")