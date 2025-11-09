from errors import ClienteError
class Cliente:
    def __init__(self, nome: str):
        self._nome = None
        self.nome = nome  

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str) or novo_nome.strip() == "":
            raise ClienteError("Nome do cliente não pode ser vazio.")
        self._nome = novo_nome.strip()

    def __str__(self):
        return self.nome
