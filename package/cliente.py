class Cliente:
    def __init__(self, nome, email, carro_listado, carro_procurado):
        self.nome = nome
        self._email = email
        self.carro_listado = carro_listado
        self.carro_procurado = carro_procurado

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        if '@' not in novo_email or '.' not in novo_email:
            raise ValueError('E-mail inválido')
        self._email = novo_email        

    def __str__(self):
        return f'Nome: {self.nome} | Vende: {self.carro_listado} | Compra: {self.carro_procurado}'