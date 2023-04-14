from telas.tela_fibonacci import TelaFibonacci
from telas.tela_inversor import TelaInvert
import PySimpleGUI as sg


class Tela():
    def __init__(self) -> None:
        None

    def criar_buttons(self):
        size = (20, 2)
        buttons = [[sg.Button('Fibonacci', size=(size), key='fibo')],
                   [sg.Button('Inverter String', size=(size), key='string')]]
        
        return [[sg.Frame('Options', expand_x=True, layout=buttons)]]
         
    def tela_main(self):
        sg.theme('LightGrey1')
        sg.set_options(font='Roboto 20 italic')

        coluna_1 = self.criar_buttons()
        coluna_2 = [[sg.Image('./Version_Grafica/img/logo_small.png')]]

        layout = [[sg.Titlebar('Desafios Target Ribeirão')],
                  [sg.Text('Desafios Target', expand_x=True, justification='center')],
                  [sg.Column(layout=coluna_1, size=(400, 300)), sg.Column('', size=(50, 300)),sg.Column(layout=coluna_2, size=(250, 300), justification='rigth')]]

        janela = sg.Window('Loucura', layout= layout, size=(700, 300))

        while True:
            event, value = janela.read()

            match event:
                case sg.WIN_CLOSED:
                    break
                case 'fibo':
                    tela = TelaFibonacci()
                    tela.tela_fibo()
                    continue
                case 'string':
                    tela = TelaInvert()
                    tela.tela_string()
                    continue
                case _:
                    break

        janela.close()