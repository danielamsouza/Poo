from funcoes import (criando_transacao, saldo, exibindo_transacao, lista_transacoes)
import funcoes

while True:
    escolha1 = input('Digite o numero da opção desejada:\n 1 - Criar nova transação\n 2 - Lista de transaçãoes\n 3 - Editar transação\n 4 - Ver o seu saldo\n 5 - Encerrar Aplicação\n')
    if escolha1 == '1':
        escolha_tipo = input('Escreva o tipo da transação: ').title()
        escolha_valor = float(input('Digite o valor da sua transacao: '))
        escolha_categoria = input('Escreva a categoria da transação: ').title()
        criando_transacao(escolha_tipo, escolha_valor, escolha_categoria)
        print(f'Transação criada com sucesso!')

    elif escolha1 == '2':
        exibindo_transacao()
        continue

    elif escolha1 == '3':
        exibindo_transacao()
        numero_transacao = int(input('Digite o numero da transação: '))
        atributo_para_editar = input('Digite o atributo que quer editar: ').lower()
        novo_valor = input('Digite o novo valor: ')
        if atributo_para_editar == 'tipo':
            lista_transacoes[numero_transacao].tipo = novo_valor.title()
        elif atributo_para_editar == 'categoria':
            lista_transacoes[numero_transacao].categoria = novo_valor.title()
        else:
            novo_valor = float(novo_valor)
            lista_transacoes[numero_transacao].valor = novo_valor
        print('Valor atualizado com sucesso!')
        continue

    elif escolha1 == '4':
        saldo()

    else:
        break