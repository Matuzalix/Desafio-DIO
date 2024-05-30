menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    limite_atingido = numero_saques >= LIMITE_SAQUES     
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor de deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Seu depósito no valor de R$ {valor:.2f} foi efetuado com sucesso!')
            
        else:
            print('Valor inválido')
        
    elif opcao == "s":
        valor = float(input("Digite o valor desejado para o saque: "))
        
        if valor > saldo:
            print("O valor Informado é maior que seu saldo atual")
            
        elif limite_atingido == True:
            print('Limite de saques diários atingido.')
            
        elif valor < saldo and valor <= limite and limite_atingido != True:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'Seu saque no valor de R$ {valor:.2f} foi efetuado com sucesso!')
            
        else:
            print("O valor solicitado é maior que seu limite de saque")
        
    elif opcao == "e":
        print(extrato)
        
    elif opcao == "q":
        break
    
    else:
        print('Opção inválida')