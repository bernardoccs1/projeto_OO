# Projeto OO - Carlisle Automóveis

Projeto completo com Desktop (Python) e Web (BMVC I, II, III, IV).

## Estrutura do Projeto

```
projeto_OO/
├── main.py                  (Desktop - Nível 1)
├── package/                 (Modelos Python)
│   ├── cadastro.py
│   ├── carro.py
│   ├── vendedor.py
│   └── ...
├── tests/                   (Testes unitários)
├── web/                     (Aplicações Web)
│   ├── bmvc-1/              (Página estática HTML/CSS/JS)
│   ├── bmvc-2/              (Backend Flask com CRUD)
│   ├── bmvc-3/              (Autenticação e Login)
│   └── bmvc-4/              (WebSocket em tempo real)
└── README.md
```

## Desktop - Nível 1

Aplicação em Python com interface de linha de comando.

### Como Executar

```bash
python main.py
```

### Funcionalidades

- Cadastrar carros
- Pesquisar carros
- Listar vendedores
- Menu interativo

---

## Web - BMVC I

Página estática com HTML, CSS e JavaScript puro.

### Como Usar

```bash
cd web/bmvc-1
# Abra o arquivo index.html em um navegador
```

### Funcionalidades

- Estrutura HTML semântica
- Estilos CSS responsivos
- Interatividade JavaScript
- Validação de formulário
- Design responsivo

---

## Web - BMVC II

Backend Flask com CRUD completo.

### Como Usar

```bash
cd web/bmvc-2
pip install flask
python app.py
# Abra http://localhost:5000
```

### Funcionalidades

- Backend em Flask
- Modelo Carro com CRUD
- Templates Jinja2
- Múltiplas páginas
- Validação de dados

---

## Web - BMVC III

Autenticação com login e página restrita.

### Como Usar

```bash
cd web/bmvc-3
pip install flask
python app.py
# Abra http://localhost:5000
# Login: admin / admin123
```

### Funcionalidades

- Sistema de login
- Autenticação de usuários
- Hash de senha SHA256
- Página restrita (dashboard)
- CRUD com isolamento de dados
- Proteção de rotas

---

## Web - BMVC IV

WebSocket para comunicação em tempo real.

### Como Usar

```bash
cd web/bmvc-4
pip install flask flask-socketio python-socketio python-engineio
python app.py
# Abra http://localhost:5000
# Login: admin / admin123
```

### Funcionalidades

- WebSocket bidirecional
- Notificações em tempo real
- Atualização assíncrona
- Modelo Notificacao
- Status de conexão em tempo real
- Animações CSS avançadas

---

## Credenciais de Teste (BMVC III e IV)

- Usuário: `admin` | Senha: `admin123`
- Usuário: `vendedor` | Senha: `vend123`

---

## Requisitos

### Desktop
- Python 3.7+

### Web
- Python 3.7+
- Flask
- Flask-SocketIO (apenas para BMVC IV)

---

## Instalação de Dependências

```bash
# Para BMVC II e III
pip install flask

# Para BMVC IV
pip install flask flask-socketio python-socketio python-engineio
```

---

## Comparação entre os Níveis

| Aspecto | Desktop | BMVC I | BMVC II | BMVC III | BMVC IV |
|---------|---------|--------|---------|----------|---------|
| Interface | CLI | HTML | Jinja2 | Jinja2 | Jinja2 + Socket.IO |
| Backend | Python | Nenhum | Flask | Flask | Flask-SocketIO |
| Banco de Dados | JSON | Nenhum | Memória | Memória | Memória |
| Autenticação | Não | Não | Não | Sim | Sim |
| CRUD | Sim | Não | Sim | Sim | Sim |
| WebSocket | Não | Não | Não | Não | Sim |
| Notificações | Não | Não | Não | Não | Sim |

---

## Autor

Desenvolvido para fins educacionais.

## Licença

Livre para uso educacional.
