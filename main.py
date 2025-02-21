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
  opcao = input(menu).strip().lower()

  if opcao == "d": # Depósito
    valor = float(input("Valor do depósito: R$ "))

    if valor <= 0:
      print("Valor inválido, tente novamente.")

    else:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f} \n"
      print("Depósito realizado com sucesso!")

  elif opcao == "s": # Saque
    valor = float(input("Valor do saque: R$ "))

    excedeu_limite = valor > limite

    saldo_insuficiente = valor > saldo

    excedeu_saques = numero_saques == LIMITE_SAQUES

    if valor <= 0:
      print("Valor inválido, tente novamente.")

    elif excedeu_limite:
      print("Falha no saque: o valor é maior que o limite permitido.")

    elif saldo_insuficiente:
      print("Falha no saque: saldo insuficiente.")

    elif excedeu_saques:
      print("Falha no saque: limite de saques diários atingido.")

    else:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f} \n"
      numero_saques += 1
      print("Saque realizado com sucesso!")

  elif opcao == "e": # Extrato
    print(" EXTRATO ".center(35, "-"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Seu saldo atual é de: R$ {saldo:.2f}")
    print("-" * 35)

  elif opcao == "q": # Sair do sistema
    break

  else:
    print("Operação inválida, por favor selecione novamente a opção desejada.")