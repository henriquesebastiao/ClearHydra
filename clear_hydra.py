import os

def clear_screen():
    os.system('clear')

def print_banner():
    print('\033[0;34mClearHydra v0.1\033[0m')
    print('Desenvolvidor por: Henrique Sebastião')
    print('https://github.com/henriquesebastiao/ClearHydra\n')

while True:
    clear_screen()
    print_banner()

    print('Escolha o protocolo para o ataque brute force:\n')
    print('1 - HTTP')
    print('2 - SSH')
    print('3 - FTP')
    print('4 - SSH (COM ESCOLHA DE UMA PORTA ESPECÍFICA)\n')

    opcao_escolhida = input('Digite a opção desejada: ')
    
    if opcao_escolhida == '1':
        pass
    elif opcao_escolhida == '2':
        endereco_ip = input('Digite o endereço IP do alvo: ').strip()
        wordlist_usuario = input('Usuário ou wordlist: ').strip()
        wordlist_senhas = input('Senha ou wordlist: ').strip
        
        print('Iniciando ataque...\n')
        
        pass
    elif opcao_escolhida == '3':
        pass
    elif opcao_escolhida == '4':
        pass
    else:
        pass