from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    tipo: str
    valor: float
    categoria: Categoria

    def exibir_transacao(self):
        print(f'Tipo de transação: {self.tipo} || Valor: {self.valor} || Categotia: {self.categoria}')
