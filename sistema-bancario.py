menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """


saldo = 0
limite = 500
extrato = """"""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valorDepositado = int(input("Informe o valor a ser depositado."))
        if valorDepositado > 0:
            saldo += valorDepositado
            extrato+= f"Depósito = R$ {valorDepositado}"
            print(saldo)
    
    elif opcao == "s":
        valorSacado = int(input("Informe o valor a ser sacado."))
        if valorSacado <= saldo:
            print("Não será possivel sacar por falta de dinheiro em conta.")
            
        elif valorSacado > 0 and numero_saques <= LIMITES_SAQUES:
            saldo -= valorSacado
            extrato+= f"Saque = R$ {valorSacado}"
            numero_saques += 1

    elif opcao == "e":
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")