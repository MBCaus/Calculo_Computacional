import os
from math import pow
import sys
import time
from tokenize import Double

while True:

    os.system('clear')

    print('------------------------------ \n' +
          '-------- Calcular IMC -------- \n' +
          '------------------------------ \n' +
          '-- [1] Calcular só o meu    -- \n' +
          '-- [2] Sair                 -- \n' +
          '------------------------------ \n')

    menu = input('Digite a função desejada: ')

    if menu == '1':

        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite seu peso: '))

        imc = round(peso/(pow(altura, 2)), 2)

        if imc < 18.5:

            cat = 'abaixo do peso'

        elif imc < 25:

            cat = 'com peso normal'

        elif imc < 30:

            cat = 'com excesso de peso'

        elif imc < 35:

            cat = 'com obesidade grau I'

        elif imc < 40:

            cat = 'com obesidade grau II'

        else:

            cat = 'com obesidade grau III'

        imc_r = str(imc)

        print('seu imc é ' + imc_r + ', logo você está ' + cat)

        exportar = input('Deseja exportar?(s / n): ')

        if exportar == 's':

            print('\n')

            arquivo = open('imc.txt', 'w')
            arquivo.write("Seu IMC: " + imc_r + "\n")
            arquivo.write("Você está " + cat)
            arquivo.close()

            # Lendo o arquivo criado:
            arquivo = open('imc.txt', 'r')
            for linha in arquivo:
                linha = linha.rstrip()
                print(linha)
            arquivo.close()

            print('\n')
            print('Exportando...')
            time.sleep(5)

        elif exportar == 'n':

            print('Voltando...')
            time.sleep(5)

        else:

            print('Valor inválido! Reiniciando programa!')
            time.sleep(5)

    elif menu == '2':

        os.system('clear')
        sys.exit()

    else:

        print('Valor inválido! Aguarde e tente novamente!')
        time.sleep(5)
