from dataclasses import dataclass

@dataclass
class Carro:
    marca: str
    modelo: str
    ligado = False

    def ligar_carro(self):
        if Carro.ligado:
            print('O carro ja esta ligado')
        else:
            Carro.ligado = True
            print('O carro esta ligado')
        return Carro.ligado

    def desligar_carro(self):
        if Carro.ligado:
            Carro.ligado = False
            print('O carro esta desligado')
        else:
            print('O carro ja esta desligado')
        return Carro.ligado

    def acelerar(self):
        if Carro.ligado:
            print('VRUUUMM')
        else:
            print('O carro esta desligado')
