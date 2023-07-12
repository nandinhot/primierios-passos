usuarios = {}
agencia = '0001'
cont = 0

print('-=-' * 20)
print(f'{"BEM VINDO AO BANCO PFTSR":^60}')
print('-=-' * 20)

while True:
    print('''Qual opção você deseja:
    [ 1 ] Cadastrar Novo Usuario:
    [ 2 ] Entrar na sua Conta:
    [ 3 ] Contas Cadastradas
    [ 4 ] Sair:''')
    opcao = input('Qual sua opção: ')

    while opcao not in ['1', '2', '3', '4']:
        print('Opção inválida. Tente novamente.')
        opcao = input('Qual sua opção: ')

    if opcao == '3':
        if len(usuarios) == 0:
            print('\033[31mNão temos nenhum usuário cadastrado. Favor fazer um cadastro para acessar o banco.\033[0m')
        else:
            print('-=-' * 20)
            print(f'{"CONTAS CADASTRADAS":^60}')
            print('-=-' * 20)
            for cpf, usuario in usuarios.items():
                print(f'Agência: {agencia:>15}')
                print(f'Conta: {usuario["conta"]:>17}')
                print(f'Nome: {usuario["nome"]:>18}')
                print(f'CPF: {cpf:>15}')
                print(f'Endereço: {usuario["endereço"]:>13}')
                print('-' * 60)

    if opcao == '4':
        break

    if opcao == '1':
        cpf = int(input('Digite seu CPF: '))
        if any(usuario['cpf'] == cpf for usuario in usuarios.values()):
            print('\033[31mUsuário já cadastrado.\033[0m')
        else:
            print('-=-' * 20)
            print(f'{"REALIZANDO CADASTRO":^60}')
            print('-=-' * 20)
            novo_usuario = {}
            novo_usuario['agencia'] = agencia
            cont += 1
            novo_usuario['conta'] = cont
            novo_usuario['nome'] = str(input('Digite seu nome completo: ')).upper()
            novo_usuario['cpf'] = cpf
            novo_usuario['endereço'] = input('Digite seu endereço: Rua: Numero: Bairro: ')
            novo_usuario['senha'] = int(input('Digite uma senha de 6 dígitos: '))
            usuarios[cpf] = novo_usuario
            print(f'{novo_usuario["nome"]} cadastrado com sucesso.')

    if opcao == '2':
        if len(usuarios) == 0:
            print('\033[31mNão temos nenhum usuário cadastrado, favor fazer um cadastro para acessar o banco.\033[0m')
        else:
            while True:
                print('-=-' * 20)
                print(f'{"VAMOS ACESSAR SUA CONTA":^60}')
                print('-=-' * 20)
                print('Para Sair a Qualquer momento digite 0: ')
                nome_usuario = input('Digite seu Nome Completo: ').upper()
                if nome_usuario == '0':
                    break
                usuario_encontrado = None
                for usuario in usuarios.values():
                    if usuario['nome'] == nome_usuario:
                        usuario_encontrado = usuario
                        break
                if usuario_encontrado:
                    senha = int(input('Digite sua senha de 6 dígitos: '))
                    if senha == usuario_encontrado['senha']:
                        print(f'Login Realizado com sucesso, bem vindo {nome_usuario}!')
                        print('-=-' * 20)
                        print(f'{"BEM VINDO AO NOSSO SISTEMA BANCÁRIO":^60}')
                        print('-=-' * 20)
                        saldo = 0
                        deposito = 0
                        saque = 0
                        quantidade_saque = 0
                        max_saque = 1000
                        extrato = ''

                        while True:
                            opcao_menu = int(input('''Escolha uma das opções a seguir:
                                [ 1 ] Sacar
                                [ 2 ] Depositar
                                [ 3 ] Visualizar Extrato
                                [ 4 ] Sair: '''))

                            if opcao_menu == 1:
                                print('-=-' * 20)
                                print(f'{"VAMOS REALIZAR UM SAQUE":^60}')
                                print('-=-' * 20)
                                valor_saque = int(input('Qual valor deseja sacar: R$ '))
                                if quantidade_saque == 3:
                                    print('Você já sacou o máximo do dia. Tente novamente amanhã.')
                                elif valor_saque > 500:
                                    print('Seu limite máximo por saque é R$500,00')
                                elif valor_saque > saldo:
                                    print(f'Você não possui saldo suficiente. Seu saldo é de R${saldo:.2f}')
                                elif valor_saque <= 0:
                                    print('Valor inválido.')
                                elif valor_saque > max_saque:
                                    print('Você não possui mais limite para saque diário.')
                                elif valor_saque <= 500:
                                    saque += valor_saque
                                    saldo -= valor_saque
                                    max_saque -= valor_saque
                                    quantidade_saque += 1
                                    extrato += f'\tSaque: R$ {valor_saque:.2f}\n'
                                    print('Saque realizado com sucesso.')

                            elif opcao_menu == 2:
                                print('-=-' * 20)
                                print(f'{"VAMOS FAZER UM DEPÓSITO":^60}')
                                print('-=-' * 20)
                                valor_deposito = float(input('Qual valor você deseja depositar: R$ '))
                                if valor_deposito > 0:
                                    deposito += valor_deposito
                                    print(f'Valor de R$ {valor_deposito:.2f} depositado com sucesso.')
                                    saldo += valor_deposito
                                    extrato += f'\tDepósito: R$ {valor_deposito:.2f}\n'
                                else:
                                    print('Valor de depósito inválido.')

                            elif opcao_menu == 3:
                                print('-=-' * 20)
                                print(f'{"EXTRATO BANCÁRIO":^60}')
                                print('-=-' * 20)
                                print('Não foram realizadas movimentações.' if not extrato else extrato)
                                print(f'Saldo disponível: R$ {saldo:.2f}')

                            elif opcao_menu == 4:
                                break

                        print('-=-' * 20)
                        print(f'{"OBRIGADO POR USAR NOSSO SISTEMA PFTSR":^60}')
                        print('-=-' * 20)
                    else:
                        print('Senha incorreta. Tente novamente.')
                else:
                    print('Usuário não cadastrado.')

print('-=-' * 20)
print(f'{"OBRIGADO POR USAR NOSSO BANCO PFTSR":^60}')
print('-=-' * 20)
