import os
from datetime import datetime

class FileAnalyzer:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__file_ada = os.path.exists(file_path)
        if self.__file_ada:
            self.__file_size = os.path.getsize(file_path)
        else:
            print(f"Error: File '{file_path}' tidak ditemukan.")        
            self.__file_size = False
            
    def get_file_size(self, unit="bytes"):
        if self.__file_ada:
            if unit.upper() == "KB":
                return round(self.__file_size / 1024, 2)
        else:
            return None
        return self.__file_size
    
    def get_modification_time(self):
        mod_time = os.path.getatime(self.__file_path)
        return datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
    
    def analyze(self):
        print("Laporan File")
        print("="*40)
        print(f"Nama File: {self.__file_path}")
        print(f"Ada?: {'Ya' if self.__file_ada else 'Tidak'}")
        if self.__file_ada:
            print(f"Ukuran File (KB): {self.get_file_size('KB')} KB")
            print(f"Waktu Modifikasi: {self.get_modification_time()}")
        else:
            print("File tidak dapat dianalisis karena tidak ditemukan")
        print("="*40)
        
analyzer1 = FileAnalyzer("dokumen.txt")
analyzer1.analyze()

analyzer2 = FileAnalyzer("file_khayalan.txt")
analyzer2.analyze()