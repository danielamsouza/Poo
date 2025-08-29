from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
    peso: float

    def editar_pessoa(self,escolha,edicao):
        if escolha == 'nome':
            self.nome = edicao
        elif escolha == 'idade':
            self.idade = edicao
        elif escolha == 'altura':
            self.altura = edicao
        else:
            self.peso = edicao