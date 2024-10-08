"""
Exercício 06 - Crie um programa onde o usuário deve adivinhar
um número gerado aleatoriamente entre 1 a 100. A cada tentativa,
exiba se ele deve tentar um número maior ou menor.
Quando o número for acertado, exiba o número de tentativas.
Dica: para gerar o número aleatório, utilize o seguinte código:
import random
numero_secreto = random.randint(1, 100)

Exemplo:
Digite um número: 50
Tente um número maior.
Digite um número: 80
Tente um número menor.
Digite um número: 61
Parabéns! Você acertou o número em 3 tentativas.
"""

import random

def random_number():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while(True):
        num = int(input("Acerte o número premiado: 1 até 100: "))
        tentativas +=1

        if(numero_secreto == num):
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
        elif(num > numero_secreto):
            print("Tente um número menor.")
        else:
            print("Tente um número maior.")
    pass

random_number()