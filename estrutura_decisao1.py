#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
lista = [ "domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado"]
x = 1

while ( x > 0):
   n = int(input("Insira um número:"))
   dia = n - 1
   if (0 <= dia < 7):
     print(" O dia da semana referente é: ",lista[dia])
     break
   else:
     print("Valor invalido. Digite novamente")
   x = x + 1
    
