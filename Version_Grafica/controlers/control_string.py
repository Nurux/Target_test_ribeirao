from classes.invert_string import Invert

class CtrInvert():
    def __init__(self) -> None:
        None

    def invert(self, string):
        if string == '':
            return 'Digite uma frase primeiro!'
        try:
            inv = Invert()
            return inv.inverter(str(string))
        except:
            return 'Ocorreu um erro ao inverter sua string!!!'