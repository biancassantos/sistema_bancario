menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Criar novo usuário
[nc] Criar nova conta
[l] Listar contas
[q] Sair

=> """

LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
numero_saques = 0
extrato = []
usuarios = []
contas = []

def deposito(valor, saldo, extrato, /):
  if valor <= 0:
    print("Valor inválido, tente novamente.")

  else:
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print("Depósito feito com sucesso!")
    return saldo


def saque(*, valor, limite, saldo, limite_saques, numero_saques, extrato):
  excedeu_limite = valor > limite
  saldo_insuficiente = valor > saldo
  excedeu_saques = numero_saques == limite_saques

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
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    print("Saque realizado com sucesso!")
    return saldo, numero_saques


def mostrar_extrato(saldo, /, *, extrato):
  print(" EXTRATO ".center(35, "-"))
  if not extrato:
    print("Não foram realizadas movimentações.")

  else:
    for movimentacao in extrato:
      print(movimentacao)

  print(f"Seu saldo atual é de: R$ {saldo:.2f}")
  print("-" * 35)


def criar_usuario(usuarios):
  cpf = input("CPF (apenas númenos): ")
  usuario_existe = filtrar_usuario(cpf, usuarios)

  if usuario_existe:
    print("Erro: Já existe um usuário com esse CPF!")
    return

  nome = input("Nome completo: ")
  data_nasc = input("Data de nascimento (dd-mm-aaaa): ")
  logradouro = input("Logradouro: ")
  numero = input("Número da residência: ")
  cidade = input("Cidade: ")
  estado = input("Estado (sigla): ")

  novo_usuario = {
    "nome": nome,
    "data_nasc": data_nasc,
    "cpf": cpf,
    "endereco": f"{logradouro}, {numero} - {cidade}/{estado}"
  }

  usuarios.append(novo_usuario)
  print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
  for usuario in usuarios:
    if usuario["cpf"] == cpf:
      return usuario
    
  return None


def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta criada com sucesso!")
    return {
      "agencia": agencia,
      "numero_conta" : numero_conta,
      "usuario": usuario
    }

  print("Erro: Usuário não encontrado!")


def listar_contas():
  print("CONTAS".center(35, "."))
  for conta in contas:
    print(f"""
    Agência: {conta["agencia"]}
    Conta: {conta["numero_conta"]}
    Titular: {conta["usuario"]["nome"]}""")
    print("." * 35)


while True:
  opcao = input(menu).strip().lower()

  if opcao == "d": # Depósito
    valor = float(input("Valor do depósito: R$ "))
    saldo = deposito(valor, saldo, extrato)

  elif opcao == "s": # Saque
    valor = float(input("Valor do saque: R$ "))
    saldo, numero_saques = saque(
      valor=valor,
      limite=limite,
      saldo=saldo,
      limite_saques=LIMITE_SAQUES,
      numero_saques=numero_saques,
      extrato=extrato
      )

  elif opcao == "e": # Extrato
    mostrar_extrato(saldo, extrato=extrato)

  elif opcao == "nu": # Criar usuário
    criar_usuario(usuarios)

  elif opcao == "nc": # Criar conta
    numero_conta = len(contas) + 1
    conta = criar_conta(AGENCIA, numero_conta, usuarios)
    if conta:
      contas.append(conta)

  elif opcao == "l": # Listar contas
    listar_contas()

  elif opcao == "q": # Sair do sistema
    break

  else:
    print("Operação inválida, por favor selecione novamente a opção desejada.")
