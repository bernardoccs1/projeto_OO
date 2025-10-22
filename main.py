import os
from package.cadastro import Cadastro

def limpar_sys(texto=''):
    os.system('cls' if os.name == 'nt' else 'clear')
    if texto:
        print(texto)

def exibir_prog():
    print('\n Carlisle Automóveis \n')

def exibir_opc():
    print('1. Cadastrar meu carro 🚗')
    print('2. Pesquisar 🔍')
    print('3. Conheça nossos vendedores 👤')
    print("4. Sair\n")

def fechar_app():
    limpar_sys('Finalizando Aplicativo...')
    exit()

def opcao_inv():
    print('Opção inválida')
    input('Pressione Enter para voltar ao menu: ')

def main():
    cadastro = Cadastro()

    while True:
        limpar_sys()
        exibir_prog()
        exibir_opc()

        try:
            escolha = int(input('Escolha uma opção: '))
            match escolha:
                case 1:
                    cadastro.cadastrar_carro()
                case 2:
                    cadastro.pesquisar_carro()
                case 3:
                    cadastro.listar_vendedores()
                case 4:
                    fechar_app()
                case _:
                    opcao_inv()
        except ValueError:
            opcao_inv()

if __name__ == '__main__':
    main()