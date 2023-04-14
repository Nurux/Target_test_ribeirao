from classes.fibonacci import Fibonacci

class CtrFibo():
    def __init__(self) -> None:
        None

    def calcular(self, num):
        if num == '':
            return 'Insira um numero primeiro!'
        try:
            fibo = Fibonacci()
            if fibo.verificar(int(num)):
                return f'O numero {num} pertence a sequencia de Fibonacci'
            return f'O numero {num} não pertence a sequencia de Fibonacci'
        except:
            return f'Digite somente numeros interos!'
