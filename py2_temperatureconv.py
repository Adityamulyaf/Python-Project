print("\tTemperature Conversion Program")

while True:
    while True:
        print("1. Celcius ke Fahrenheit")
        print("2. Fahrenheit ke Celcius")
        unit = input("Masukkan unit (1/2): ")

        if unit in ['1', '2']:
            break
        else:
            print("Unit tidak valid! Silakan coba lagi.")

    if unit == '1':
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = round((celsius * 9/5) + 32, 2)
        print(f"{celsius} °C = {fahrenheit} °F")
    elif unit == '2':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = round((fahrenheit - 32) * 5/9, 2)
        print(f"{fahrenheit} °F = {celsius} °C")

    lanjut = input("Konvert lagi? (y/n): ")
    if lanjut.lower() != 'y':
        print("Program selesai.")
        break
