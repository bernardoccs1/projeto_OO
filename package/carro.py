class Carro:
    def __init__(self, marca_modelo, ano, preco, placa):
        self.marca_modelo = marca_modelo
        self.ano = ano
        self.__preco = float(preco)
        self.placa = placa
        self._ativo = True
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco<0:
            raise ValueError('Preço não pode ser valor negativo')
        self.__preco = novo_preco

    @property
    def status(self):
        return 'Disponível' if self._ativo else 'Vendido'
    
    def vender(self):
        self._ativo = False

    def reativar(self):
        self._ativo = True

    def __str__(self):
        return f'{self.marca_modelo} {self.ano} | Placa {self.placa} - R$ {self.preco:.2f}'