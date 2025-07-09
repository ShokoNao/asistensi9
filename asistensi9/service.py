# service.py

from model import Dokter # Mengimpor kelas Dokter dari file model.py

class JadwalDokter:
    """Kelas untuk mengelola jadwal dokter (Business Logic)"""
    def __init__(self):
        """Inisialisasi dengan daftar dokter awal"""
        self.dokters = [
            Dokter('Indri', 'Umum', ['Senin', 'Rabu', 'Jumat'], '08:00 - 12:00'),
            Dokter('Jeno', 'Anak', ['Selasa', 'Kamis'], '09:00 - 13:00'),
            Dokter('Jaemin', 'Gigi', ['Senin', 'Kamis'], '10:00 - 14:00'),
            Dokter('Jisung', 'Umum', ['Rabu', 'Jumat'], '08:00 - 12:00'),
            Dokter('Jaehyun', 'Kandungan', ['Senin', 'Rabu'], '13:00 - 17:00'),
            Dokter('Taeyong', 'Anak', ['Jumat'], '09:00 - 12:00'),
            Dokter('Musawwir', 'Umum', ['Senin', 'Selasa'], '10:00 - 14:00'),
            Dokter('Joseph', 'Umum', ['Minggu', 'Rabu'], '00:00 - 05:00')
        ]
    
    def get_all_schedules(self):
        """Mengembalikan semua data dokter"""
        return self.dokters
    
    def get_schedules_sorted_by_name(self):
        """Mengembalikan semua data dokter diurutkan berdasarkan nama"""
        return sorted(self.dokters, key=lambda dokter: dokter.nama.lower())

    def get_schedules_grouped_by_day(self):
        """Mengembalikan jadwal yang dikelompokkan berdasarkan hari"""
        urutan_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        jadwal_per_hari = {hari: [] for hari in urutan_hari}
        for dokter in self.dokters:
            for hari in dokter.hari:
                if hari in jadwal_per_hari:
                    jadwal_per_hari[hari].append(dokter)
        return jadwal_per_hari

    def find_by_specialist(self, spesialis):
        """Mencari dokter berdasarkan spesialis"""
        return [d for d in self.dokters if d.spesialis.lower() == spesialis.lower()]

    def find_by_day(self, hari):
        """Mencari dokter berdasarkan hari"""
        return [d for d in self.dokters if hari.capitalize() in d.hari]

    def find_by_name(self, nama):
        """Mencari dokter berdasarkan nama"""
        return [d for d in self.dokters if nama.lower() in d.nama.lower()]

    def add_doctor(self, nama, spesialis, hari, jam):
        """Menambah dokter baru"""
        hari_list = [h.strip().capitalize() for h in hari.split(',')]
        self.dokters.append(Dokter(nama, spesialis, hari_list, jam))
        return True

    def remove_doctor(self, nama):
        """Menghapus dokter berdasarkan nama"""
        dokter_awal_count = len(self.dokters)
        self.dokters = [d for d in self.dokters if d.nama.lower() != nama.lower()]
        return len(self.dokters) < dokter_awal_count