from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    numero_de_paginas: int

meu_livro = Livro('Uma Breve Historia do Tempo', 'Stephen Hawking', 300)

print(meu_livro.autor)