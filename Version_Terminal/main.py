from classes.invert_string import Invert
from classes.fibonacci import Fibonacci
from os import system

def verifica_fibonacci(num):
    calculo = Fibonacci()
    
    if calculo.verificar(num):
        return f'O numero {num} pertence a sequencia de Fibonacci'
    
    return f'O numero {num} não pertence a sequencia de Fibonacci'

def inverter_string(string):
    inversor = Invert()
    return inversor.inverter(string)

def limpa_tela():
    input('Aperte Enter para voltar ao menu')
    system('cls')
    
def menu():
    return print('''
    --------------------\n
       Desafios Target\n
    --------------------\n
    1 - Fibonacci\n
    2 - Invert String\n
    3 - Sair\n 
    ''')

def main():
    while True: 
        menu()

        op = int(input())

        match op:
            case 1:
                num = int(input('Digite um numero intero: '))
                print(verifica_fibonacci(num))
                limpa_tela()
                continue
            case 2:
                string = str(input('Digite uma frase: '))
                print(inverter_string(string))
                limpa_tela()
                continue
            case 3:
                break
            case _:
                print('Escolha uma das opções!')
                continue

if __name__ == '__main__':
    main()