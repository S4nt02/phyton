#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = int(input("Digite um número: "))

centenas = n // 100
resto = n % 100

dezenas = resto // 10
unidade = resto - ( dezenas * 10 )




if ( centenas > 1 ):
    if ( dezenas > 1 ):
        if ( unidade > 1 ):
            print("O número digitado foi {}, ele possui {} centenas, {} dezenas e {} unidades".format( n, centenas, dezenas, unidade))
        elif ( unidade == 0 ):
            print("O número digitado foi {}, ele possui {} centenas e {} dezenas ".format(n ,centenas, dezenas))
        elif ( unidade == 1 ):
            print("O número digitado foi {}, ele possui {} centenas, {} dezenas e {} unidade".format( n, centenas, dezenas, unidade))
    elif ( dezenas == 0 ):
        if ( unidade > 1):
            print("O número digitado foi {}, ele possui {} centenas e {} unidades".format( n, centenas, unidade))
        elif ( unidade == 1 ):
            print("O número digitado foi {}, ele possui {} centenas e {} unidade".format( n, centenas, unidade))
        elif ( unidade == 0 ):
            print("O número digitado foi {}, ele possui {} centenas".format( n, centenas))
    elif ( dezenas == 1 ):
        if ( unidade > 1 ):
            print("O número digitado foi {}, ele possui {} centenas, {} dezena e {} unidades".format( n, centenas, dezenas, unidade))
        elif ( unidade == 0 ):
            print("O número digitado foi {}, ele possui {} centenas e {} dezena ".format(n ,centenas, dezenas))
        elif ( unidade == 1 ):
            print("O número digitado foi {}, ele possui {} centenas, {} dezena e {} unidade".format( n, centenas, dezenas, unidade))

        
elif ( centenas == 1 ):
      if ( dezenas > 1 ):
           if ( unidade > 1 ):
              print("O número digitado foi {}, ele possui {} centena, {} dezenas e {} unidades".format( n, centenas, dezenas, unidade))
           elif ( unidade == 0 ):
              print("O número digitado foi {}, ele possui {} centena e {} dezenas ".format(n ,centenas, dezenas))
           elif ( unidade == 1 ):
              print("O número digitado foi {}, ele possui {} centena, {} dezenas e {} unidade".format( n, centenas, dezenas, unidade))
      elif ( dezenas == 0 ):
           if ( unidade > 1):
              print("O número digitado foi {}, ele possui {} centena e {} unidades".format( n, centenas, unidade))
           elif ( unidade == 1 ):
              print("O número digitado foi {}, ele possui {} centena e {} unidade".format( n, centenas, unidade))
           elif ( unidade == 0 ):
              print("O número digitado foi {}, ele possui {} centena".format( n, centenas))
      elif ( dezenas == 1 ):
           if ( unidade > 1 ):
              print("O número digitado foi {}, ele possui {} centena, {} dezena e {} unidades".format( n, centenas, dezenas, unidade))
           elif ( unidade == 0 ):
              print("O número digitado foi {}, ele possui {} centena e {} dezena ".format(n ,centenas, dezenas))
           elif ( unidade == 1 ):
              print("O número digitado foi {}, ele possui {} centena, {} dezena e {} unidade".format( n, centenas, dezenas, unidade))
elif ( centenas == 0 ):
     if ( dezenas > 1 ):
           if ( unidade > 1 ):
              print("O número digitado foi {}, ele possui, {} dezenas e {} unidades".format( n, dezenas, unidade))
           elif ( unidade == 0 ):
              print("O número digitado foi {}, ele possui {} dezenas ".format(n , dezenas))
           elif ( unidade == 1 ):
              print("O número digitado foi {}, ele possui {} dezenas e {} unidade".format( n, dezenas, unidade))
     elif ( dezenas == 0):
           if ( unidade > 1):
              print("O número digitado foi {}, ele possui {} unidades".format( n, unidade))
           elif ( unidade == 1 ):
              print("O número digitado foi {}, ele possui {} unidade".format( n, unidade))
     elif ( dezenas == 1 ):
           if ( unidade > 1 ):
              print("O número digitado foi {}, ele possui {} dezena e {} unidades".format( n, dezenas, unidade))
           elif ( unidade == 0 ):
              print("O número digitado foi {}, ele possui {} dezena ".format(n , dezenas))
           elif ( unidade == 1 ):
              print("O número digitado foi {}, ele possui {} dezena e {} unidade".format( n, dezenas, unidade))
    

