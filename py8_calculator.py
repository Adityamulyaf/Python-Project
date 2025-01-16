while True:
    operator = input("Masukkan operasi (+, -, *, /): ")

    if operator in ['+', '-', '*', '/']:
        break
    else:
        print("Operator tidak valid! Silakan coba lagi.")

num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))

if operator == '+':
    result = num1 + num2
    print(f"Hasil {num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"Hasil {num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"Hasil {num1} * {num2} = {result}")

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Hasil {num1} / {num2} = {round(result, 3)}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")