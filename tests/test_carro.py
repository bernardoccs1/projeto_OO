import pytest
from package.carro import Carro

def test_criacao_carro():
    carro = Carro('Civic', 2020, 95000, 'ABC-1234')
    assert carro.marca_modelo == 'Civic'
    assert carro.preco == 95000
    assert carro.status == 'Disponível'

def test_vender_reativar_carro():
    carro = Carro('Civic', 2020, 95000, 'ABC-1234')
    carro.vender()
    assert carro.status == 'Vendido'
    carro.reativar()
    assert carro.status == 'Disponível'

def test_preco_nao_pode_ser_negativo():
    carro = Carro('Civic', 2020, 95000, 'ABC-1234')
    with pytest.raises(ValueError):
        carro.preco = -10
