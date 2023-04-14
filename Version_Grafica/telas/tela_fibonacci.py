from controlers.control_fibo import CtrFibo
import PySimpleGUI as sg

class TelaFibonacci():
    def __init__(self) -> None:
        None
    
    def tela_fibo(self):
        sg.theme('LightGrey1')

        layout = [[sg.Titlebar('Verificador de Fibonacci')],
                  [sg.Text('Digite um numero inteiro: ')],
                  [sg.InputText('', key='num')],
                  [sg.Button('Verificar', key='ver'), sg.Button('Sair', key='exit')],
                  [sg.Text('', key='output', visible=False)]]
        
        janela = sg.Window('Fibonacci', layout= layout)

        while True:
            event, value = janela.read()

            match event:
                case sg.WIN_CLOSED:
                    break
                case 'ver':
                    verificador = CtrFibo()
                    janela['output'].update(verificador.calcular(value['num']), visible=True)
                    continue
                case 'exit':
                    break
                case _: 
                    break
        
        janela.close()