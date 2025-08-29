from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    tipo: str
    valor: float
    categoria: Categoria

    def exibindo_transacao1(self):
        print(f'Id da transação: {self} || Tipo: {self.tipo} || Valor: {self.valor} || Categoria: {self.categoria}')

    def editando_transacao(self, tipo, valor, categoria):
        self.tipo = tipo
        self.valor = valor
        self.categoria = Categoria
