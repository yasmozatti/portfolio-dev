class User:
    id : int
    nome: str
    identificador : str
    documento : int

    def __init__(self, id, nome, identificador, documento):
        self.id = id
        self.nome = nome
        self.identificador = identificador
        self.documento = documento

class Administrador(User):
    def __init___(self, id, name, identificador, documento):
        super.__init__()