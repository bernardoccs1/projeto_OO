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
