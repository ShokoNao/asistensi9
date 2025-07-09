# model.py

class Dokter:
    """Kelas untuk menyimpan data dokter (Data Model)"""
    def __init__(self, nama, spesialis, hari, jam):
        """Inisialisasi data dokter"""
        self.nama = nama
        self.spesialis = spesialis
        self.hari = hari
        self.jam = jam