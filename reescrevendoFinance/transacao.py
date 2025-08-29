from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    tipo: str
    valor: float
    categoria: Categoria
