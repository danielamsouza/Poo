from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    tipo: str
    valor: float
    categoria: Categoria

    def editar_transacao(self, dado, valor):
        if dado == 'tipo':
            self.tipo = valor
        elif dado == 'valor':
            self.valor = valor
        else:
            self.categoria = Categoria(valor)

    def exibir_transacao(self):
        print(f'Tipo de transação: {self.tipo} || Valor: {self.valor} || Categotia: {self.categoria}')
