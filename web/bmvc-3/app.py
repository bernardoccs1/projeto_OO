from flask import Flask, render_template, request, redirect, url_for, session
from models import Usuario, Carro
from functools import wraps

app = Flask(__name__)
app.secret_key = 'chave_secreta_carlisle'

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
                Carro.criar(marca, modelo, preco, ano, session['usuario_id'])
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
                Carro.atualizar(id, marca, modelo, preco, ano)
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
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
