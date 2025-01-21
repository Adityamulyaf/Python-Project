# Compound Interest = Bunga Majemuk
# Rumus A = P x (1 + r)^t
# A = jumlah akhir
# P = investasi awal
# r = rate/tingkat bunga per periode
# n = jumlah periode

import math

principle = 0
rate = 0
time = 0

print("\t<<< INTEREST COMPOUND CALCULATOR >>>\n")

while True:
    principle = float(input("Masukkan investasi awal: $"))
    if principle <= 0:
        print("Investasi awal tidak boleh <= 0")
    else: break

while True:
    rate = float(input("Masukkan rate bunga (dalam persen): "))
    if rate <= 0:
        print("Rate tidak boleh <= 0")
    else: break

while True:
    time = float(input("Masukkan periode investasi (dalam tahun): "))
    if time <= 0:
        print("Periode investasi tidak boleh <= 0")
    else: break

print(f"\nInvestasi awal: ${principle}")
print(f"Rate bunga: {rate} %")
print(f"Periode investasi: {time} tahun")

jumlah_akhir = principle * pow((1 + rate/100), time)

print("\nJumlah akhir = Investasi awal x (1 + rate) ^ periode investasi")
print(f"Jumlah akhir = {principle} x (1 + {rate/100}) ^ {time}")
print(f"Jumlah akhir = ${round(jumlah_akhir, 2)}")
