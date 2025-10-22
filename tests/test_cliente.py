import pytest
from package.cliente import Cliente

def test_cliente_email_valido():
    cliente = Cliente('Bernardo', 'bernardo@email.com', 'Civic', 'Onix')
    assert cliente.email == 'bernardo@email.com'

def test_cliente_email_invalido():
    cliente = Cliente('Bernardo', 'teste@email.com', 'Civic', 'Onix')
    with pytest.raises(ValueError):
        cliente.email = 'bernardo#semarroba'
