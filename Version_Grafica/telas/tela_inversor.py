from controlers.control_string import CtrInvert
import PySimpleGUI as sg

class TelaInvert():
    def __init__(self) -> None:
        None
    
    def tela_string(self):
        sg.theme('LightGrey1')

        layout = [
            [sg.Titlebar('Inversor de Strings')],
            [sg.Text('Digite uma frase qualquer')],
            [sg.InputText('', key='string')],
            [sg.Button('Inversor', key='inv'), sg.Button('Sair', key='exit')],
            [sg.Text('', key='output', visible=False)]
        ]

        janela = sg.Window('String', layout= layout)

        while True:
            event, value = janela.read()

            match event:
                case sg.WIN_CLOSED:
                    break
                case 'inv':
                    inversor = CtrInvert()
                    janela['output'].update(inversor.invert(value['string']), visible=True)
                    continue
                case 'sair':
                    break
                case _:
                    break
        
        janela.close()