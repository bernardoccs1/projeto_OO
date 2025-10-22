from .carro import Carro
from .cliente import Cliente
from .vendedor import Vendedor
import json

class Cadastro:
    def __init__(self):
        self.carros = []
        self.vendedores = [
            Vendedor('Davi', 16, 6),
            Vendedor('Bernardo', 20, 4),
            Vendedor('Enrico', 30, 8)
        ]
        self.clientes = []
        self.clientes = []

#Funções relacionadas a carros/carro.py#

    def cadastrar_carro(self):
        marca_modelo = input('Marca e modelo do veículo : ')
        ano = input('Ano: ')
        placa = input('Placa do veículo: ')
        preco = input('Preço: R$ ')
        
        carro = Carro(marca_modelo, ano, preco, placa)
        self.carros.append(carro)
        print(f'\n Carro cadastrado com sucesso!\n')
        input('Pressione Enter p/ voltar ao menu')

    def listar_carro(self):
        if not self.carros:
            print('Nenhum carro cadastrado.')
        else:
            print('\n--- Carros disponíveis ---')
            for c in self.carros:
                print(c)
            print('---------------------------\n')
        input('Pressione Enter p/ voltar ao menu')

    def pesquisar_carro(self):
        termo = input('Digite parte do modelo ou placa: ')
        resultados = [c for c in self.carros if termo.lower() in c.marca_modelo.lower() or termo.lower() in c.placa.lower()]
        if resultados:
            for c in resultados:
                print(c)
        else:
            print('Nenhum carro encontrado.')
        input('Pressione Enter p/ voltar ao menu')


#Funções relacionada a vendedores/vendedor.py#

    def cadastrar_vendedores(self):
        nome = input('Nome: ')
        vendas_mes = int(input('Vendas do mês: '))
        clientes_momento = int(input('Clientes atuais: '))
        vendedor = Vendedor(nome, vendas_mes, clientes_momento)
        self.vendedores.append(vendedor)
        print(f'\n Vendedor {nome} cadastrado! \n')
        input('Pressione Enter p/ voltar ao menu')

    def listar_vendedores(self):
        if not self.vendedores:
            print('Não há vendedores')
        else:
            print ('\n Vendedores \n')
            for v in self.vendedores:
                print (v)
        input('\n Pressione Enter p/ voltar ao menu \n')

    def func_do_mes(self):
        if not self.vendedores:
            print('Nenhum funcionário do mês')
            return
        melhor = max(self.vendedores, key=lambda v: v.vendas_mes)
        print (f'Funcionário do Mẽs: {melhor.nome}')
        input('\n Pressione Enter p/ voltar ao menu')
    
#Funções relacionadas a clientes/cliente.py#

    def cadastrar_cliente(self):
        nome = input('Nome do cliente: ')
        email = input('E-mail: ')
        carro_listado = input('Carro que está vendendo: ')
        carro_procurado = input('Carro que está procurando: ')
        cliente = Cliente(nome, email, carro_listado, carro_procurado)
        self.clientes.append(cliente)
        print(f'\n Cliente {nome} cadastrado! \n')
        input('Pressione Enter p/ voltar ao menu')

    def listar_clientes(self):
        if not self.clientes:
            print('Nenhum cliente cadastrado')
        else:
            print('----- Clientes Cadastrados -----')
            for c in self.clientes:
                print(c)
            print(' --------------------------------')
        input('Pressione Enter p/ voltar ao menu')