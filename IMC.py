import os
from math import pow
import sys
import time
from tokenize import Double

while True:

    os.system('clear')
    os.system('cls')

    print('------------------------------ \n' +
          '-------- Calcular IMC -------- \n' +
          '------------------------------ \n' +
          '-- [1] Calcular só o meu    -- \n' +
          '-- [2] Calcular mais que 1  -- \n' +
          '-- [3] Sair                 -- \n' +
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
        cont = 0
        qtd = int(input('Quantos IMCs você quer calcular: '))

        num = 0
        a = 0

        while qtd > cont:

            altura = float(input('Digite sua altura: '))
            peso = float(input('Digite seu peso: '))

            imc = round(peso/(pow(altura, 2)), 2)

            cont = cont + 1

            imc_r = str(imc)

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

            v_imc = []
            v_cat = []
            v_resul = []

            v_imc.append(imc_r)
            v_cat.append(cat)

            num = num + 1
            
            num_r = str(num)

            print('\n')
            print(num_r + '. IMC é ' + imc_r + ', logo você está ' + cat)
            print('\n')


            v_resul.insert(a, num_r + '. IMC é ' + imc_r +
                           ', logo você está ' + cat)

            a = a + 1

            print(v_resul)

            time.sleep(2)

        print('------------------------------')

        tam = len(v_resul)

        for i in range(tam):
            item = v_resul.pop()
            print(item)

        print('------------------------------')

        print('\n')

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

    elif menu == '3':

        os.system('clear')
        sys.exit()

    else:

        print('Valor inválido! Aguarde e tente novamente!')
        time.sleep(5)
