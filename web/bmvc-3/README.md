# BMVC III - Carlisle Automóveis

Projeto completo com autenticação de usuários, login, página restrita e CRUD.

## Requisitos

- Python 3.7+
- Flask

## Instalação

```bash
pip install flask
```

## Como Executar

```bash
python app.py
```

Abra http://localhost:5000 no navegador.

## Credenciais de Teste

- Usuário: `admin` | Senha: `admin123`
- Usuário: `vendedor` | Senha: `vend123`

## Funcionalidades

- Sistema de login com autenticação
- Página restrita (dashboard)
- CRUD completo de carros
- Isolamento de dados por usuário
- Hash de senha SHA256
- Logout e proteção de rotas

## Arquitetura

- **Backend:** Flask (app.py)
- **Modelos:** Usuario e Carro (models.py)
- **Frontend:** Templates Jinja2
- **Autenticação:** Session e decorator
- **Segurança:** Hash de senha, proteção de rotas

## Dados Iniciais

**Usuário admin:**
- BMW X5 2024 - R$ 450.000
- Mercedes C-Class - R$ 380.000

**Usuário vendedor:**
- Audi A4 2024 - R$ 420.000
