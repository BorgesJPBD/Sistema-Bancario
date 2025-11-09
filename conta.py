
from cliente import Cliente
from errors import ContaError, ValorInvalidoError, SaldoInsuficienteError


class ContaBancaria:
    _proximo_numero = 1  

    def __init__(self, cliente: Cliente, saldo_inicial: float = 0.0):
        if not isinstance(cliente, Cliente):
            raise ContaError("Titular deve ser um objeto Cliente.")
        self._cliente = cliente
        self._saldo = 0.0
        if saldo_inicial > 0:
            self.depositar(saldo_inicial)
        self._numero = ContaBancaria._proximo_numero
        ContaBancaria._proximo_numero += 1

    

    @property
    def titular(self) -> Cliente:
        """Retorna o cliente (titular) da conta."""
        return self._cliente

    @property
    def saldo(self) -> float:
        """Saldo atual (somente leitura)."""
        return self._saldo

    @property
    def numero(self) -> int:
        """Número da conta (somente leitura)."""
        return self._numero

    
    def depositar(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError("Valor do depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValorInvalidoError("Valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
        self._saldo -= valor

    def transferir(self, outra_conta: "ContaBancaria", valor: float):
        from errors import ContaError  

        if not isinstance(outra_conta, ContaBancaria):
            raise ContaError("A conta de destino deve ser uma ContaBancaria.")
        self.sacar(valor)         
        outra_conta.depositar(valor)

    def resumo(self) -> str:
        return (
            f"Conta {self.numero} | Titular: {self.titular.nome} "
            f"| Saldo: R$ {self.saldo:.2f}"
        )

    def exibir_resumo(self):
        print(self.resumo())
