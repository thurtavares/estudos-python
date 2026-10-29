def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

temperatura = float(input("Digite a temperatura em Celsius: "))
print(celsius_para_fahrenheit(temperatura))
