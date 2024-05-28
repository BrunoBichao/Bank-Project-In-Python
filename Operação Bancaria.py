menu = """
================================== M E N U ===================================
[1] Depositar                                                      Extrato [3]
[2] Sacar                                                             Sair [0]
==============================================================================
Operação:"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nInforme o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("\nOperação falhou! O valor informado é inválido.")


    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if exedeu_saldo:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor de saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\nOperação falhou! O valor informado é inválido.")

        
    elif opcao == "3":
        print("\n================================== EXTRATO ===================================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================================================================")

    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    



