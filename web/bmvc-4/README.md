# BMVC IV - Carlisle Automóveis

Projeto completo com autenticação, login, página restrita, CRUD e WebSocket em tempo real.

## Requisitos

- Python 3.7+
- Flask
- Flask-SocketIO

## Instalação

```bash
pip install flask flask-socketio python-socketio python-engineio
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
- WebSocket para comunicação em tempo real
- Notificações em tempo real
- Atualização assíncrona da lista
- Isolamento de dados por usuário
- Hash de senha SHA256
- Logout e proteção de rotas

## Arquitetura

- **Backend:** Flask + Flask-SocketIO
- **Modelos:** Usuario, Carro, Notificacao
- **Frontend:** Templates Jinja2 + WebSocket
- **Autenticação:** Session + decorator
- **Comunicação:** WebSocket bidirecional
- **Segurança:** Hash de senha, proteção de rotas

## Dados Iniciais

**Usuário admin:**
- BMW X5 2024 - R$ 450.000
- Mercedes C-Class - R$ 380.000

**Usuário vendedor:**
- Audi A4 2024 - R$ 420.000

## Notas

- Os dados são armazenados em memória
- Quando o servidor é reiniciado, os dados são perdidos
- Para persistência, seria necessário usar um banco de dados
- As senhas são hash com SHA256
- WebSocket permite comunicação em tempo real entre cliente e servidor
