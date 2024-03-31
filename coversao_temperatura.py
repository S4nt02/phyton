# Escreva um programa que converta uma temperatura digitada em ºC em ºF. A formula
# para conversão é:

# F = (9xC)/5 + 32

c = float(input("Digite a temperatura em graus Celcius:"))
f = (9 * c) / 5 + 32
print("A tempperatura em fahrenheit é:",f)