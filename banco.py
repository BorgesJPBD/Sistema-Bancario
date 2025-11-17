from errors import ValorInvalidoError
from cliente import Cliente
from conta import ContaBancaria

class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.contas = []

    def criar_conta(self, nome_titular: str, saldo_inicial: float = 0.0):
        if not nome_titular.strip():
            raise ValorInvalidoError("O nome do titular não pode ser vazio.")

        
        if saldo_inicial == 0:
            raise ValorInvalidoError("O saldo inicial não pode ser zero.")

        if saldo_inicial < 0:
            raise ValorInvalidoError("O saldo inicial não pode ser negativo.")

        titular = Cliente(nome_titular)
        conta = ContaBancaria(titular, saldo_inicial)
        self.contas.append(conta)
        return conta
