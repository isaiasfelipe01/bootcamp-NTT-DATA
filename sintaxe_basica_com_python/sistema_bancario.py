def divisoria():
    return print('-' * 30)


menu = """
--- Escolha uma opção ---

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

-> """

numero_operacao = 0
saldo = 0
limite = 500
numero_saques = 1
LIMITE_SAQUE = 3
historico_de_transacoes = {'operacao': [], 'valor': [], 'transacao': []}

while True:
    opcao = input(menu).lower()
    
    if opcao == 'd':
        divisoria()
        deposito = float(input('Valor de Deposito: R$'))
        if deposito > 0:
            saldo += deposito
            numero_operacao += 1
            historico_de_transacoes['operacao'].append('deposito')
            historico_de_transacoes['valor'].append(deposito)
            historico_de_transacoes['transacao'].append(numero_operacao)
        else:
            print('Valor inválido. Tente novamente.')
        divisoria()
    elif opcao == 's':
        divisoria()
        if numero_saques <= LIMITE_SAQUE and saldo > 0:
            numero_saques += 1
            numero_operacao += 1
            while True:
                saque = float(input('Valor de Saque: R$'))
                if saque <= limite and saque > 0 and saque <= saldo:
                    saldo -= saque
                    historico_de_transacoes['operacao'].append('saque')
                    historico_de_transacoes['valor'].append(-saque)
                    historico_de_transacoes['transacao'].append(numero_operacao)
                    break
                elif saque > limite:
                    print('Você está tentando sacar um valor maior que o limite de saque.\nO valor máximo é R$500,00.')
                elif saque > saldo:
                    print('Saldo indisponível.')
                else:
                    print('Valor invalido. Tente novamente.')
        elif saldo == 0:
            print('Você não possui saldo disponível para saque.')
        elif numero_saques >= LIMITE_SAQUE:
            print('Você atingiu o limite de saques diários.')
        
        divisoria()
    elif opcao == 'e':
        if not historico_de_transacoes['operacao']:
            print('Não há transações para mostrar.')
            continue
        else:
            print('-' * 36)
            print(f"{'Nº transação':<12} {'Operação':<10} {'Valor':<10}")
            print('-' * 36)
            for i in range(len(historico_de_transacoes['operacao'])):
                transacao = historico_de_transacoes['transacao'][i]
                operacao = historico_de_transacoes['operacao'][i]
                valor = historico_de_transacoes['valor'][i]
                print(f"{transacao:<12} {operacao:<10} R$ {valor:<10.2f}")
            print('-' * 36)

            print(f'Saldo: R${saldo:.2f}')
            print('-' * 17)

    elif opcao == 'q':
        break