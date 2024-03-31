#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

lista = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]
saltos = []
soma = 0
atleta = input("insira o nome do atleta:")


for x in range(5):
   if (atleta == ""):
     print("nome do atleta não digitado")
     break 
   else:
         salto = float(input("digite o valor para o {} salto: ".format( lista [ x ] ) ) )
         saltos.append ( salto )
         soma = soma + salto
         
ordem_saltos = sorted(saltos)

print(" Atleta: ", atleta )
print("Primeiro salto: ",saltos [ 0 ] )
print("Segundo salto: ",saltos [ 1 ]  )
print("Terceiro salto: ",saltos [ 2 ]  )
print("Quarto Salto: ",saltos [ 3 ]  )
print("Quinto salto: ",saltos [ 4 ]  )
print("Melhor salto: ",ordem_saltos[ 4 ]  )
print("Pior salto: ",ordem_saltos [ 0 ] )

media = ( ordem_saltos[1] + ordem_saltos[2] + ordem_saltos[3]) / 3
print("Média dos demais saltos: ",media )
print("Resultado final: {}: {} m".format(atleta, media))
      
