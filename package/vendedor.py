class Vendedor:
    def __init__(self, nome, vendas_mes, clientes_momento):
        self.nome = nome
        self._vendas_mes = vendas_mes
        self._clientes_momento = clientes_momento

    @property
    def vendas_mes(self):
        return self._vendas_mes
        
    @vendas_mes.setter
    def vendas_mes(self, valor):
        if valor < 0:
            raise ValueError('Valor negativo não permitido')
        self._vendas_mes = valor
    
    @property
    def clientes_momento(self):
        return self._clientes_momento

    @clientes_momento.setter
    def clientes_momento(self, valor):
        if valor < 0:
            raise ValueError('Valor negativo não permitido')
        if valor > 30:
            print(f'Aviso: {self.nome} não pode exceder o número de 35 mês')
        else:
            self._clientes_momento = valor

    def __str__(self):
        return f' {self.nome} | Realizou {self.vendas_mes} vendas neste mês! | Atendendo {self.clientes_momento} clientes na semana \n'