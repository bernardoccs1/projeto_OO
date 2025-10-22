from package.cadastro import Cadastro
from package.carro import Carro

def test_cadastro_carros():
    cad = Cadastro()
    cad.carros.append(Carro('Civic', 2020, 95000, 'ABC-1234'))
    assert len(cad.carros) == 1
    assert cad.carros[0].marca_modelo == 'Civic'

def test_pesquisar_carro():
    cad = Cadastro()
    cad.carros.append(Carro('Civic', 2020, 95000, 'ABC-1234'))
    cad.carros.append(Carro('Onix', 2022, 70000, 'XYZ-9876'))
    resultados = [c for c in cad.carros if 'Civic' in c.marca_modelo]
    assert len(resultados) == 1
    assert resultados[0].placa == 'ABC-1234'
