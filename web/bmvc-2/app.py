from flask import Flask, render_template, request, redirect, url_for
from models import Carro

app = Flask(__name__)

Carro.criar('BMW', 'X5 2024', 450000, 2024)
Carro.criar('Mercedes', 'C-Class', 380000, 2023)
Carro.criar('Audi', 'A4 2024', 420000, 2024)

@app.route('/')
def index():
    carros = Carro.obter_todos()
    return render_template('index.html', carros=carros)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/criar', methods=['POST'])
def criar():
    marca = request.form.get('marca')
    modelo = request.form.get('modelo')
    preco = request.form.get('preco')
    ano = request.form.get('ano')
    
    if marca and modelo and preco and ano:
        try:
            preco = float(preco)
            ano = int(ano)
            Carro.criar(marca, modelo, preco, ano)
        except ValueError:
            pass
    
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    carro = Carro.obter_por_id(id)
    if not carro:
        return redirect(url_for('index'))
    return render_template('editar.html', carro=carro)

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    marca = request.form.get('marca')
    modelo = request.form.get('modelo')
    preco = request.form.get('preco')
    ano = request.form.get('ano')
    
    if marca and modelo and preco and ano:
        try:
            preco = float(preco)
            ano = int(ano)
            Carro.atualizar(id, marca, modelo, preco, ano)
        except ValueError:
            pass
    
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    Carro.deletar(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
