# Nama = ("osep")
# umur = 10 
# tinggi = 170
# print (umur + tinggi)

# Hujan = "Deras" 

# if Hujan  == "grimis":
#     print ("yaps kamu benar")
# else:
#     print ("anda salah")

import random

welcome_message = "WELCOME TO MY GAMES"
monster_position = random.randint(1, 4)

print("**********************")
print(f"* {welcome_message} *")
print("**********************")

nama = input("Masukkan nama anda: ")

print(f'''
Halo {nama} Coba perhatikan goa dibawah ini:
|_| |_| |_| |_|
''')

pilihan_user = input("Menurut Anda goa berapa yang terisi oleh monster? [1 / 2 / 3 / 4]: ")

konfirmasi = input("Apakah anda yakin? [yes/no]: ")

if konfirmasi == "yes":
    pilihan_user = (pilihan_user)  # Konversi input pengguna menjadi integer
    
    if pilihan_user == monster_position:
        print(f"SELAMAT {nama} ANDA MENANG! POSISI MONSTER ADA DI {monster_position} DAN PILIHAN MU {pilihan_user}")
    else:
        print(f"MAAF ANDA KALAH! POSISI MONSTER ADA DI {monster_position} SEMENTARA ANDA MEMILIH {pilihan_user}")
else:
    print("Anda membatalkan permainan.")
