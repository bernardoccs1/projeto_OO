class Carro:
    contador_id = 1
    carros = []
    
    def __init__(self, marca, modelo, preco, ano):
        self.id = Carro.contador_id
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
        Carro.contador_id += 1
    
    @classmethod
    def criar(cls, marca, modelo, preco, ano):
        carro = cls(marca, modelo, preco, ano)
        cls.carros.append(carro)
        return carro
    
    @classmethod
    def obter_todos(cls):
        return cls.carros
    
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
    
    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'preco': self.preco,
            'ano': self.ano
        }
