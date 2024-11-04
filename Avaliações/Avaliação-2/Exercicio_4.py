class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def exibir_informacoes(self):
        print(f"Titular: {self.titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")


class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, limite_cheque_especial):
        super().__init__(numero_conta, titular)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if valor <= self.saldo + self.limite_cheque_especial:
            self.saldo -= valor
        else:
            print("Saque não permitido: saldo insuficiente.")


class ContaPoupanca(ContaBancaria):
    taxa_juros = 0.05

    def sacar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print("Saque não permitido: saldo insuficiente.")

    def calcular_saldo(self):
        return self.saldo + (self.saldo * self.taxa_juros)


if __name__ == "__main__":
    tipo_conta = input("Digite o tipo da conta (corrente/poupanca): ").strip().lower()
    numero_conta = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")

    if tipo_conta == "corrente":
        limite_cheque_especial = float(input("Digite o limite do cheque especial: "))
        conta = ContaCorrente(numero_conta, titular, limite_cheque_especial)
    elif tipo_conta == "poupanca":
        conta = ContaPoupanca(numero_conta, titular)
    else:
        print("Tipo de conta inválido.")
        exit()

    while True:
        acao = input("\nEscolha uma ação: depositar, sacar, exibir, ou sair: ").strip().lower()

        if acao == "depositar":
            valor = float(input("Digite o valor a depositar: "))
            conta.depositar(valor)
        elif acao == "sacar":
            valor = float(input("Digite o valor a sacar: "))
            conta.sacar(valor)
        elif acao == "exibir":
            conta.exibir_informacoes()
        elif acao == "sair":
            break
        else:
            print("Ação inválida.")