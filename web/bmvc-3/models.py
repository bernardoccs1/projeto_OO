import hashlib

class Usuario:
    usuarios = []
    
    def __init__(self, username, email, senha):
        self.id = len(Usuario.usuarios) + 1
        self.username = username
        self.email = email
        self.senha = self._hash_senha(senha)
    
    @staticmethod
    def _hash_senha(senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    @classmethod
    def registrar(cls, username, email, senha):
        if cls.obter_por_username(username):
            return None
        usuario = cls(username, email, senha)
        cls.usuarios.append(usuario)
        return usuario
    
    @classmethod
    def login(cls, username, senha):
        usuario = cls.obter_por_username(username)
        if usuario and usuario.senha == cls._hash_senha(senha):
            return usuario
        return None
    
    @classmethod
    def obter_por_username(cls, username):
        for usuario in cls.usuarios:
            if usuario.username == username:
                return usuario
        return None
    
    @classmethod
    def obter_por_id(cls, id):
        for usuario in cls.usuarios:
            if usuario.id == id:
                return usuario
        return None


class Carro:
    contador_id = 1
    carros = []
    
    def __init__(self, marca, modelo, preco, ano, usuario_id):
        self.id = Carro.contador_id
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
        self.usuario_id = usuario_id
        Carro.contador_id += 1
    
    @classmethod
    def criar(cls, marca, modelo, preco, ano, usuario_id):
        carro = cls(marca, modelo, preco, ano, usuario_id)
        cls.carros.append(carro)
        return carro
    
    @classmethod
    def obter_por_usuario(cls, usuario_id):
        return [c for c in cls.carros if c.usuario_id == usuario_id]
    
    @classmethod
    def obter_por_id(cls, id):
        for carro in cls.carros:
            if carro.id == id:
                return carro
        return None
    
    @classmethod
    def atualizar(cls, id, marca, modelo, preco, ano):
        carro = cls.obter_por_id(id)
        if carro:
            carro.marca = marca
            carro.modelo = modelo
            carro.preco = preco
            carro.ano = ano
            return carro
        return None
    
    @classmethod
    def deletar(cls, id):
        carro = cls.obter_por_id(id)
        if carro:
            cls.carros.remove(carro)
            return True
        return False
