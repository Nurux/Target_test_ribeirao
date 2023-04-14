class Invert():
    def __init__(self) -> None:
        None


    def inverter(self, string):
        new_string = ''

        for i in range(len(string)):
            new_string += string[len(string) -i -1]
        
        return new_string