import pytest
from package.vendedor import Vendedor

def test_vendedor_criacao():
    vendedor = Vendedor('João', 10, 5)
    assert vendedor.vendas_mes == 10
    assert vendedor.clientes_momento == 5

def test_vendas_invalidas():
    vendedor = Vendedor('João', 10, 5)
    with pytest.raises(ValueError):
        vendedor.vendas_mes = -1

def test_clientes_limite():
    vendedor = Vendedor('Maria', 8, 5)
    vendedor.clientes_momento = 12 
