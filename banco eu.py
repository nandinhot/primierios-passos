print('-=-' *20)
print(f'{"BEM VINDO AO NOSSO SISTEMA BANCARIO":^60}')
print('-=-' *20)
saldo = 0
deposito = 0
saque = 0
quantidade_saque = 0
max_saque = 1000
extrato = ''


# loop
while True:
    opcao = int(input('''Escolha uma das opções a Seguir:
[ 1 ] Sacar
[ 2 ] Depositar
[ 3 ] Visualizar Extrato
[ 4 ] Sair:    '''))

    if opcao == 1:
        print('-=-' *20)
        print(f'{"VAMOS REALIZAR UM SAQUE":^60}')
        print('-=-' *20)
        valor_saque =int(input('Qual Valor Deseja Sacar: R$ '))
        if quantidade_saque == 3:
            print('Você Ja Sacou o Maximo do dia, tente novamente amanha:')
        elif valor_saque > 500:
            print('Seu Limite maximo por saque é R$500,00')
        elif valor_saque > saldo:
            print(f'Você não possui saldo Suficiente, o seu saldo é de R${saldo:.2f}')
        elif valor_saque <= 0:
            print(f'Valor Invalido.')
        elif valor_saque > max_saque:
            print(f'Você não pussiu mas limite para saque diario.')
        elif valor_saque <=500:
            saque += valor_saque
            saldo -= valor_saque
            max_saque -= valor_saque
            quantidade_saque +=1
            extrato += f'Saque : R$ {valor_saque:.2f}\n'
            print('Saque Realizado com Sucesso:')        
        
    if opcao == 2:
        print('-=-' *20)
        print(f'{"VAMOS FAZER UM DEPOSITO":^60}')
        print('-=-' *20)
        dep = 0
        while True:
            dep = int(input('Qual Valor Você deseja depositar: R$ '))
            if dep >0:
                deposito += dep
                print(f'Valor de R$ {dep:.2f} depositado com sucesso.')
                saldo += dep
                extrato += f'Depósito: R$ {dep:.2f}\n'
                break
            else:
                print('Valor depositado não pode ser negativo:')
                break
    if opcao == 3:
        print('-=-' *20)
        print(f'{"EXTRATO BANCARIO":^60}')
        print('-=-' *20)
        print('\nNão foram realizaadas movimentações:' if not extrato else extrato)
        print(f'\nSaldo disponivel: R$ {saldo:.2f}')
      
    if opcao == 4:
        break
print('-=-' *20)
print(f'{"OBRIGADO POR USAR NOSSO SISTEMA PFTSR":^60}')
print('-=-' *20)
