from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from models import Usuario, Carro, Notificacao
from functools import wraps

app = Flask(__name__)
app.secret_key = 'chave_secreta_carlisle'
socketio = SocketIO(app, cors_allowed_origins="*")

usuarios_conectados = {}

Usuario.registrar('admin', 'admin@carlisle.com', 'admin123')
Usuario.registrar('vendedor', 'vendedor@carlisle.com', 'vend123')

usuario_admin = Usuario.obter_por_username('admin')
Carro.criar('BMW', 'X5 2024', 450000, 2024, usuario_admin.id)
Carro.criar('Mercedes', 'C-Class', 380000, 2023, usuario_admin.id)

usuario_vend = Usuario.obter_por_username('vendedor')
Carro.criar('Audi', 'A4 2024', 420000, 2024, usuario_vend.id)

def requer_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('senha')
        usuario = Usuario.login(username, senha)
        
        if usuario:
            session['usuario_id'] = usuario.id
            session['username'] = usuario.username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@requer_login
def dashboard():
    usuario_id = session['usuario_id']
    carros = Carro.obter_por_usuario(usuario_id)
    return render_template('dashboard.html', carros=carros)

@app.route('/novo', methods=['GET', 'POST'])
@requer_login
def novo():
    if request.method == 'POST':
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        preco = request.form.get('preco')
        ano = request.form.get('ano')
        
        if marca and modelo and preco and ano:
            try:
                preco = float(preco)
                ano = int(ano)
                carro = Carro.criar(marca, modelo, preco, ano, session['usuario_id'])
                Notificacao.criar('sucesso', f'Carro {marca} {modelo} adicionado com sucesso!', session['usuario_id'])
                socketio.emit('carro_adicionado', carro.to_dict(), room=f"user_{session['usuario_id']}")
                return redirect(url_for('dashboard'))
            except ValueError:
                pass
    
    return render_template('novo.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
@requer_login
def editar(id):
    carro = Carro.obter_por_id(id)
    
    if not carro or carro.usuario_id != session['usuario_id']:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        preco = request.form.get('preco')
        ano = request.form.get('ano')
        
        if marca and modelo and preco and ano:
            try:
                preco = float(preco)
                ano = int(ano)
                carro = Carro.atualizar(id, marca, modelo, preco, ano)
                Notificacao.criar('info', f'Carro ID {id} atualizado com sucesso!', session['usuario_id'])
                socketio.emit('carro_atualizado', carro.to_dict(), room=f"user_{session['usuario_id']}")
                return redirect(url_for('dashboard'))
            except ValueError:
                pass
    
    return render_template('editar.html', carro=carro)

@app.route('/deletar/<int:id>')
@requer_login
def deletar(id):
    carro = Carro.obter_por_id(id)
    
    if carro and carro.usuario_id == session['usuario_id']:
        Carro.deletar(id)
        Notificacao.criar('aviso', f'Carro ID {id} removido com sucesso!', session['usuario_id'])
        socketio.emit('carro_deletado', {'id': id}, room=f"user_{session['usuario_id']}")
    
    return redirect(url_for('dashboard'))

@socketio.on('connect')
def handle_connect():
    if 'usuario_id' in session:
        usuario_id = session['usuario_id']
        username = session['username']
        join_room(f"user_{usuario_id}")
        usuarios_conectados[request.sid] = {'usuario_id': usuario_id, 'username': username}
        emit('usuario_conectado', {'username': username})

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in usuarios_conectados:
        del usuarios_conectados[request.sid]

@socketio.on('solicitar_notificacoes')
def handle_solicitar_notificacoes():
    if 'usuario_id' in session:
        notificacoes = Notificacao.obter_ultimas(session['usuario_id'])
        emit('notificacoes_atualizadas', {
            'notificacoes': [n.to_dict() for n in notificacoes]
        })

@socketio.on('solicitar_carros')
def handle_solicitar_carros():
    if 'usuario_id' in session:
        carros = Carro.obter_por_usuario(session['usuario_id'])
        emit('lista_carros_atualizada', {
            'carros': [c.to_dict() for c in carros]
        })

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
