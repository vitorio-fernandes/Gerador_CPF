import random

while True:
    try:
        entrada = int(input("Digite a quantidade de CPF que deseja: "))
        for i in range(entrada):
            cpf = ""
            for i in range(9):
                cpf += str(random.randint(0, 9))

            contador_regressivo = 10
            soma = 0

            for numero in cpf:
                soma += int(numero) * contador_regressivo
                contador_regressivo -= 1

            digito_1 = 11 - (soma % 11)
            if digito_1 > 9:
                digito_1 = 0

            cpf += str(digito_1)

            contador_regressivo = 11
            soma = 0

            for numero in cpf:
                soma += int(numero) * contador_regressivo
                contador_regressivo -= 1

            digito_2 = 11 - (soma % 11)
            if digito_2 > 9:
                digito_2 = 0

            cpf += str(digito_2)

            cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:11])
            print(cpf)

    except:
        print("Insira valores inteiros !\n")
