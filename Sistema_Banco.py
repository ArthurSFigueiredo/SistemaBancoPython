# Deposito, saque e extrato - OPERAÇÕES PRINCIPAIS

# DEPÓSITO - possível somente depósitos positivos, os depósitos devem ser armazenados em uma variável e exibidos na operação EXTRATO

# SAQUE - poderá realizar 3 saques diários com limite máximo de R%500,00 por saque, caso não tenha saldo em conta, o sistema deve exibir "Não é possível realizar o saque, saldo insuficiente", todos os saques devem ser armazenados em uma variável e exibidos na operação EXTRATO

#EXTRATO - deve listar todos os depósitos e saques, no fim da listagem exibir saldo atual da conta, o formato deve ser: R$ xxx.xx

menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            print("Depósito realizado com Sucesso!")
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou, Valor inválido")
        
    elif opcao == "2":

        saque = float(input("Informe o valor do saque: "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite = saque > limite
        excedeu_saldo = saque > saldo

        if excedeu_saques:
            print("O limite de saques foi atingido, operação não concluída")

        elif excedeu_limite:
            print("O valor de saque excede o limite de R$500.00, operação não concluída")

        elif excedeu_saldo:
            print("O valor de saque é maior que o saldo, operação não concluída")

        elif  saque > 0 and saque <= saldo and saque <= limite:
            print("Saque realizado com Sucesso!")
            numero_saques += 1
            saldo -= saque
            extrato += f"Saque de: R$ {saque:.2f}\n"
        
        else:
            print("Não é possível realizar o saque, saldo insuficiente/ número de saques diários atingidos/ saque acima do limite máximo de R$500,00")
    
    elif opcao == "3":
        print(f""" 
--------------- EXTRATO DA CONTA ----------------
{extrato}

Saldo atual: R${saldo: .2f}
-------------------------------------------------
        """)
        
    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione uma das opções disponíveis")
