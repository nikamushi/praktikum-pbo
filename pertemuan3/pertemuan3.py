class User:
    def __init__(self, username, level):
        self.__username = ""
        self.__level = ""
        self.set_username(username)
        self.set_level(level)
        
    def info(self):
        print(f"Username: {self.__username}, Level: {self.__level}")
        
    def get_username(self):
        return self.__username
    
    def get_level(self):
        return self.__level
    
    # --- Setter Methods dengan validasi ---
    def set_username(self, username_baru):
        if (len(username_baru) > 5):
            print("Username berhasil diubah.")
        else:
            print("Error: Username terlalu pendek! Minimal 6 karakter.")
    
    def set_level(self, level_baru):
        allowed_levels = ["User", "Admin", "Super Admin"]
        if level_baru in allowed_levels:
            self.__level = level_baru
            print("Level berhasil diubah.")
        else:
            print(f"Error: level '{level_baru}' tidak valid")
        
user_1 = User("admin_ganteng", "Super Admin")
user_1.info()

print("\n--- Mencoba mengubah data via setter ---")
user_1.set_username("admin") # ini akan gagal
user_1.set_level("Moderator") # ini akan gagal
user_1.info() # data tidak berubah

print("\n--- Mencoba lagi dengan data yang valid ---")
user_1.set_username("Administrator_sistem")
user_1.set_level("Admin")
user_1.info()