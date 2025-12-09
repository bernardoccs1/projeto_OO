# Roteiro de Vídeo - BMVC IV

## Introdução

Este é um projeto BMVC IV completo com autenticação de usuários, login, página restrita, CRUD e comunicação WebSocket em tempo real. Demonstra a arquitetura completa com Backend em Python (Flask-SocketIO), Modelos de dados, Views em HTML/Jinja2, Controllers (Rotas Flask) e comunicação assíncrona em tempo real.

---

## Apresentação da Estrutura

Mostrar a pasta do projeto e explicar a estrutura:

```
bmvc-4/
├── app.py              (Backend Flask com SocketIO)
├── models.py           (Modelos: Usuario, Carro, Notificacao)
├── templates/
│   ├── base.html       (Template base com WebSocket)
│   ├── login.html      (Página de login)
│   ├── dashboard.html  (Página restrita com WebSocket)
│   ├── novo.html       (Criar carro)
│   └── editar.html     (Editar carro)
└── static/
    ├── css/style.css   (Estilos com animações)
    └── js/script.js    (WebSocket e interatividade)
```

Explicar que este projeto é diferente do anterior porque agora temos:
- Comunicação WebSocket em tempo real
- Notificações em tempo real
- Atualização assíncrona da lista de carros
- Modelo de Notificação
- Animações para eventos em tempo real

---

## Iniciar o Servidor

Abrir terminal e executar:
```bash
pip install flask-socketio python-socketio python-engineio
python app.py
```

Mostrar a mensagem que o servidor está rodando na porta 5000 com SocketIO ativado.

---

## Demonstração do Login

Abrir http://localhost:5000 no navegador.

Mostrar que é redirecionado automaticamente para a página de login.

Fazer login com o usuário "admin" / "admin123".

Mostrar que após o login, você é redirecionado para o dashboard.

Observar o indicador de conexão que muda para "Conectado" em verde.

---

## Demonstração do WebSocket - Status de Conexão

Na página do dashboard, mostrar o indicador de conexão em tempo real.

Explicar que o status muda automaticamente quando a conexão WebSocket é estabelecida.

Abrir o console do navegador (F12) para mostrar as mensagens de conexão.

---

## Demonstração do CRUD com WebSocket - CREATE

Clicar em "Novo Carro".

Preencher o formulário com um novo carro (ex: Toyota Corolla, 250000, 2024).

Clicar em "Salvar".

Observar que:
1. Uma notificação aparece no canto superior direito em tempo real
2. A página redireciona para o dashboard
3. O novo carro aparece na tabela com uma animação de destaque verde
4. A notificação desaparece automaticamente após 3 segundos

---

## Demonstração do CRUD com WebSocket - UPDATE

Clicar em "Editar" em um dos carros.

Modificar um campo (ex: mudar o preço).

Clicar em "Atualizar".

Observar que:
1. Uma notificação de "Carro atualizado" aparece
2. A linha do carro na tabela é destacada em verde
3. Os dados são atualizados em tempo real sem recarregar a página

---

## Demonstração do CRUD com WebSocket - DELETE

Clicar em "Deletar" em um carro.

Confirmar a deleção.

Observar que:
1. Uma notificação de "Carro removido" aparece
2. A linha do carro desaparece da tabela com uma animação suave
3. A tabela é atualizada em tempo real

---

## Demonstração de Múltiplas Abas (Opcional)

Abrir o dashboard em duas abas diferentes do navegador.

Fazer login em ambas com o mesmo usuário.

Criar um novo carro em uma aba.

Observar que a outra aba também recebe a notificação e atualiza a lista em tempo real.

Explicar que isso é possível graças ao WebSocket que mantém a comunicação bidirecional.

---

## Mostrar o Código - Modelos (models.py)

Abrir o arquivo models.py.

Mostrar a classe Usuario com autenticação.

Mostrar a classe Carro com dados e timestamp.

Mostrar a classe Notificacao com:
- Método criar() para criar notificações
- Método obter_ultimas() para recuperar histórico
- Método to_dict() para serialização

Explicar que as notificações são armazenadas em memória com limite de 50.

---

## Mostrar o Código - Backend (app.py)

Abrir o arquivo app.py.

Mostrar:
- Importação de SocketIO
- Inicialização do SocketIO
- Decorador @socketio.on('connect') para conexão
- Decorador @socketio.on('disconnect') para desconexão
- Emissão de eventos com emit()
- Uso de rooms para isolar usuários

Explicar o fluxo:
1. Cliente conecta via WebSocket
2. Servidor recebe evento 'connect'
3. Servidor adiciona cliente a uma room específica do usuário
4. Quando há mudança (criar, editar, deletar), servidor emite evento
5. Cliente recebe evento e atualiza a página em tempo real

---

## Mostrar o Código - Frontend (script.js)

Abrir o arquivo script.js.

Mostrar:
- Inicialização do socket: `const socket = io();`
- Listeners de eventos: `socket.on('carro_adicionado', ...)`
- Emissão de eventos: `socket.emit('solicitar_carros')`
- Funções de atualização de UI: `mostrarNotificacao()`, `atualizarLinha()`, `removerLinha()`

Explicar que o JavaScript puro gerencia toda a comunicação WebSocket.

---

## Mostrar o Código - CSS com Animações

Abrir o arquivo style.css.

Mostrar:
- Animação `slideIn` para notificações
- Animação `highlight` para linhas atualizadas
- Animação `slideOut` para linhas deletadas
- Estilos para status de conexão (verde/vermelho)

Explicar que as animações melhoram a experiência do usuário.

---

## Demonstração de Responsividade

Redimensionar a janela do navegador.

Mostrar que a página se adapta em telas pequenas.

Mostrar que as notificações também se adaptam.

---

## Explicar a Arquitetura BMVC IV

### Backend (app.py - Flask + SocketIO)
- Define rotas HTTP
- Gerencia conexões WebSocket
- Emite eventos em tempo real
- Mantém rooms por usuário
- Valida autenticação

### Model (models.py - Classes)
- Classe Usuario: autenticação, hash de senha
- Classe Carro: CRUD, isolamento por usuário
- Classe Notificacao: histórico de eventos
- Métodos to_dict() para serialização JSON

### View (templates/*.html - Jinja2)
- login.html: formulário de autenticação
- dashboard.html: página restrita com WebSocket
- novo.html: formulário para criar
- editar.html: formulário para editar
- base.html: template base com script.io

### Controller (app.py - Rotas + SocketIO)
- Rotas HTTP para CRUD
- Eventos WebSocket para atualizações em tempo real
- Proteção de rotas com decorator
- Isolamento de dados por usuário

---

## Diferenças do BMVC III para BMVC IV

| Aspecto | BMVC III | BMVC IV |
|---------|----------|---------|
| Autenticação | Sim | Sim |
| Login | Sim | Sim |
| Página Restrita | Sim | Sim |
| CRUD | Sim | Sim |
| WebSocket | Não | Sim |
| Notificações | Não | Sim |
| Atualização em Tempo Real | Não | Sim |
| Modelo de Notificação | Não | Sim |
| Animações | Básicas | Avançadas |
| Comunicação Assíncrona | Não | Sim |

---

## Funcionalidades Implementadas

✓ **Autenticação de Usuários** - Login com validação
✓ **Hash de Senha** - SHA256 para segurança
✓ **Página Restrita** - Dashboard protegido
✓ **Isolamento de Dados** - Cada usuário vê seus dados
✓ **CRUD Completo** - Create, Read, Update, Delete
✓ **WebSocket** - Comunicação bidirecional em tempo real
✓ **Notificações em Tempo Real** - Feedback imediato
✓ **Atualização Assíncrona** - Sem recarregar página
✓ **Animações** - Transições suaves
✓ **Múltiplas Páginas** - Login, Dashboard, Novo, Editar
✓ **Logout** - Limpeza de sessão
✓ **Responsividade** - Funciona em mobile

---

## Credenciais de Teste

**Usuário 1:**
- Username: admin
- Senha: admin123
- Carros: 2 (BMW X5, Mercedes C-Class)

**Usuário 2:**
- Username: vendedor
- Senha: vend123
- Carros: 1 (Audi A4)

---

## Requisitos Atendidos

✓ Vídeo de no máximo 15 minutos
✓ Modelos em Python (Usuario, Carro, Notificacao)
✓ Múltiplas páginas HTML
✓ CRUD completo
✓ Sistema de LOGIN
✓ Página de acesso restrito
✓ WebSocket para comunicação em tempo real
✓ Atualização assíncrona de dados
✓ Informações legíveis
✓ Propósito claro (gerenciar carros com autenticação e WebSocket)
✓ CSS funcional com animações
✓ JS funcional com WebSocket
✓ Código personalizado
✓ Arquitetura BMVC completa

---

## Dicas para Apresentação

1. Comece mostrando a estrutura do projeto
2. Inicie o servidor e acesse a página
3. Demonstre o login funcionando
4. Mostre o status de conexão WebSocket
5. Demonstre cada operação CRUD com WebSocket
6. Observe as notificações em tempo real
7. Observe as animações de atualização
8. Teste a responsividade
9. Mostre o código dos modelos
10. Mostre o código do backend com SocketIO
11. Mostre o código do frontend com WebSocket
12. Explique a arquitetura BMVC IV
13. Respeite o tempo máximo de 15 minutos

---

## Checklist

- [ ] Servidor iniciado corretamente
- [ ] Login funcionando
- [ ] WebSocket conectado (status verde)
- [ ] CREATE com notificação em tempo real
- [ ] READ com lista atualizada
- [ ] UPDATE com animação de destaque
- [ ] DELETE com animação de remoção
- [ ] Notificações aparecendo e desaparecendo
- [ ] Responsividade funcionando
- [ ] Vídeo gravado
- [ ] Vídeo com no máximo 15 minutos
