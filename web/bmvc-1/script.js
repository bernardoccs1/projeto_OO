const btnExplorar = document.getElementById('btnExplorar');
const formulario = document.getElementById('formulario');
const botoesDetalhes = document.querySelectorAll('.btn-detalhes');

btnExplorar.addEventListener('click', () => {
    document.getElementById('carros').scrollIntoView({ behavior: 'smooth' });
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();
    
    if (!nome || !email || !mensagem) {
        alert('Preencha todos os campos');
        return;
    }
    
    if (!validarEmail(email)) {
        alert('Email inválido');
        return;
    }
    
    alert(`Obrigado ${nome}! Sua mensagem foi enviada.`);
    formulario.reset();
});

function validarEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

botoesDetalhes.forEach(botao => {
    botao.addEventListener('click', function() {
        const nomeCarro = this.parentElement.querySelector('h3').textContent;
        alert(`Você selecionou: ${nomeCarro}`);
    });
});
