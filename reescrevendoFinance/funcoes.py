from categoria import Categoria
from transacao import Transacao

lista_transacoes = []

def criando_transacao(tipo, valor, categoria):
    transacao = Transacao(tipo, valor, categoria)
    lista_transacoes.append(transacao)
    return transacao

def saldo():
    saldo = 0
    for i in lista_transacoes:
        saldo += i.valor
    print(f'Saldo: R${saldo}')

def exibindo_transacao():
    indice = 0
    for i in lista_transacoes:
        print(f'{indice} - {i}')
        indice += 1