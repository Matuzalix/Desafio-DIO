contas = []

def criar_conta(nome, sobrenome, cpf, saldo_inicial):
    
    conta = {
        'nome': nome,
        'sobrenome': sobrenome,
        'cpf': cpf,
        'saldo': saldo_inicial
    }
    contas.append(conta)
    print(f"Conta criada com sucesso para {nome} {sobrenome}.")

def listar_contas():
    
    if not contas:
        print("Nenhuma conta encontrada.")
    else:
        for conta in contas:
            print(f"Nome: {conta['nome']} {conta['sobrenome']}, CPF: {conta['cpf']}, Saldo: R${conta['saldo']}")

def buscar_conta(cpf):
    
    for conta in contas:
        if conta['cpf'] == cpf:
            return conta
    return None

def exibir_conta(cpf):
    
    conta = buscar_conta(cpf)
    if conta:
        print(f"Nome: {conta['nome']} {conta['sobrenome']}, CPF: {conta['cpf']}, Saldo: R${conta['saldo']}")
    else:
        print(f"Nenhuma conta encontrada para o CPF {cpf}.")

def depositar(cpf, valor):
    
    conta = buscar_conta(cpf)
    if conta:
        conta['saldo'] += valor
        print(f"Depósito de R${valor} realizado com sucesso para {conta['nome']} {conta['sobrenome']}.")
    else:
        print(f"Nenhuma conta encontrada para o CPF {cpf}.")

def sacar(cpf, valor):
    
    conta = buscar_conta(cpf)
    if conta:
        if conta['saldo'] >= valor:
            conta['saldo'] -= valor
            print(f"Saque de R${valor} realizado com sucesso para {conta['nome']} {conta['sobrenome']}.")
        else:
            print(f"Saldo insuficiente para saque na conta de {conta['nome']} {conta['sobrenome']}.")
    else:
        print(f"Nenhuma conta encontrada para o CPF {cpf}.")

def menu():
    
    while True:
        opcao = input("""
[1] Criar conta
[2] Depositar
[3] Sacar
[4] Extrato
[5] Listar Contas
[6] Sair

=> """)
        
        if opcao == '1':
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            cpf = input("CPF: ")
            saldo_inicial = float(input("Saldo inicial: R$"))
            criar_conta(nome, sobrenome, cpf, saldo_inicial)
        elif opcao == '2':
            cpf = input("CPF da conta para depósito: ")
            valor = float(input("Valor do depósito: R$"))
            depositar(cpf, valor)
        elif opcao == '3':
            cpf = input("CPF da conta para saque: ")
            valor = float(input("Valor do saque: R$"))
            sacar(cpf, valor)
        elif opcao == '4':
            cpf = input("CPF da conta: ")
            exibir_conta(cpf)
        elif opcao == '5':
            listar_contas()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
