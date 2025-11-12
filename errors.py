
class BancoError(Exception):
    """Erro genérico do sistema bancário."""
    pass


class ValorInvalidoError(BancoError):
    """Valor numérico inválido (negativo, zero, etc.)."""
    pass


class SaldoInsuficienteError(BancoError):
    """Tentativa de saque/transferência sem saldo suficiente."""
    pass


class ContaNaoEncontradaError(BancoError):
    """Conta não foi encontrada pelo número informado."""
    pass


class NomeObrigatorioError(BancoError):
    """Nome do titular é obrigatório."""
    pass


class OpcaoInvalidaError(BancoError):
    """Opção do menu inválida."""
    pass


class OperacaoCanceladaError(BancoError):
    """Usuário cancelou a operação."""
    pass


class LimiteSaqueExcedidoError(BancoError):
    """Saque acima do limite permitido (por operação ou diário)."""
    pass


class LimiteTransferenciaExcedidoError(BancoError):
    """Transferência acima do limite permitido."""
    pass


class ContaJaExisteError(BancoError):
    """Já existe uma conta com este identificador (ex: CPF)."""
    pass
