#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input("Digite a quantidade de termos: "))
m = n + 1
soma = 0
for x in range(1, m):
        soma = soma + x
print(soma)
