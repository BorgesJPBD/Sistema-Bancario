
class BancoError(Exception):
    """Erro base para o sistema bancário."""
    pass


class ClienteError(BancoError):
    """Erros relacionados ao cliente."""
    pass


class ContaError(BancoError):
    """Erros relacionados à conta."""
    pass


class ValorInvalidoError(ContaError):
    """Quando o valor informado é inválido (ex: negativo ou zero)."""
    pass


class SaldoInsuficienteError(ContaError):
    """Quando não há saldo suficiente para a operação."""
    pass


class ContaNaoEncontradaError(ContaError):
    """Quando uma conta não é encontrada pelo número."""
    pass
