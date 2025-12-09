const socket = io();

socket.on('connect', function() {
    atualizarStatusConexao(true);
    socket.emit('solicitar_notificacoes');
    socket.emit('solicitar_carros');
});

socket.on('disconnect', function() {
    atualizarStatusConexao(false);
});

socket.on('usuario_conectado', function(data) {
    mostrarNotificacao('sucesso', `${data.username} conectado com sucesso!`);
});

socket.on('carro_adicionado', function(carro) {
    mostrarNotificacao('sucesso', `Carro ${carro.marca} ${carro.modelo} adicionado!`);
    atualizarLista();
});

socket.on('carro_atualizado', function(carro) {
    mostrarNotificacao('info', `Carro ID ${carro.id} atualizado!`);
    atualizarLinha(carro);
});

socket.on('carro_deletado', function(data) {
    mostrarNotificacao('aviso', `Carro ID ${data.id} removido!`);
    removerLinha(data.id);
});

socket.on('notificacoes_atualizadas', function(data) {
    data.notificacoes.forEach(notif => {
        mostrarNotificacao(notif.tipo, notif.mensagem);
    });
});

socket.on('lista_carros_atualizada', function(data) {
    console.log('Lista de carros atualizada:', data.carros);
});

function atualizarStatusConexao(conectado) {
    const statusEl = document.getElementById('status-conexao');
    if (statusEl) {
        if (conectado) {
            statusEl.textContent = 'Conectado';
            statusEl.className = 'status-conectado';
        } else {
            statusEl.textContent = 'Desconectado';
            statusEl.className = 'status-desconectado';
        }
    }
}

function mostrarNotificacao(tipo, mensagem) {
    const container = document.getElementById('notificacoes');
    if (!container) return;

    const notif = document.createElement('div');
    notif.className = `notificacao ${tipo}`;
    notif.textContent = mensagem;

    container.appendChild(notif);

    setTimeout(() => {
        notif.style.animation = 'slideOut 0.3s ease-in-out';
        setTimeout(() => notif.remove(), 300);
    }, 3000);
}

function atualizarLinha(carro) {
    const tbody = document.getElementById('carros-tbody');
    if (!tbody) return;

    let linha = document.querySelector(`tr[data-id="${carro.id}"]`);
    if (linha) {
        linha.classList.add('atualizado');
        setTimeout(() => linha.classList.remove('atualizado'), 500);
    }
}

function removerLinha(id) {
    const linha = document.querySelector(`tr[data-id="${id}"]`);
    if (linha) {
        linha.style.animation = 'slideOut 0.3s ease-in-out';
        setTimeout(() => linha.remove(), 300);
    }
}

function atualizarLista() {
    socket.emit('solicitar_carros');
}

document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href*="deletar"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            if (!confirm('Tem certeza que deseja deletar este carro?')) {
                e.preventDefault();
            }
        });
    });
});
