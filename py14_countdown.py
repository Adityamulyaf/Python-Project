import time

waktu = int(input("Masukkan waktu dalam detik: "))

for x in range (waktu, 0, -1):
    detik = x % 60
    menit = int(x / 60) % 60
    jam = int(x / 3600)
    
    print(f"{jam:02}:{menit:02}:{detik:02}")
    time.sleep(1)

print("WAKTU HABIS!")