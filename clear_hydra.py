import os, time, re

# Cores
colors = {
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'darkcyan': '\033[36m',
    'blue': '\033[94m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'end': '\033[0m'
}

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

# Função para verificar se o IP é válido
def check_ip(ip):
    if(re.search(regex, ip)):
        return True
    else:
        return False

# Função para verificar se o diretório existe
def directory_exists(directory):
    if os.path.isdir(directory):
        return True
    else:
        return False

# Função para limpar a tela
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Função para imprimir o banner
def print_banner():
    with open('banner.txt', 'r') as banner:
        for line in banner:
            print(line, end='')
    print('\n')
    print(time.strftime('%d/%m/%Y', time.localtime()) + ' ' + time.strftime('%H:%M:%S', time.localtime()))
    print('''Desenvolvidor por: Henrique Sebastião
https://github.com/henriquesebastiao/ClearHydra\n
''')

# Função para retornar a porta padrão do protocolo
def default_port(protocol):
    match protocol:
        case '1':
            return '80'
        case '2':
            return '22'
        case '3':
            return '23'
        case '4':
            return '21'

# Escolha do protocolo
while True:
    clear_screen()
    print_banner()

    print('''Escolha o protocolo para o ataque brute force:\n
1 - HTTP
2 - SSH
3 - Telnet
4 - FTP
''')

    protocol_name = ''
    chosen_option = input('Escolha uma opção: ').strip()
    
    if chosen_option in ['1', '2', '3', '4']:
        clear_screen()
        
        # Define o nome do protocolo
        match chosen_option:
            case '1':
                protocol_name = 'http-get'
            case '2':
                protocol_name = 'ssh'
            case '3':
                protocol_name = 'telnet'
            case '4':
                protocol_name = 'ftp'
        break
    else:
        print('\nOpção inválida!')
        print('Tente novamente...\n')
        time.sleep(1.3)

# Escolha da porta
while True:
    print_banner()
    print('''1 - Porta padrão
2 - Porta específica\n
''')
    port_option = input('Escolha uma opção: ').strip()
    
    match port_option:
        case '1':
            port = default_port(chosen_option)
            clear_screen()
            print_banner()
            break
        case '2':
            clear_screen()
            print_banner()
            port = input('Digite a porta: ').strip()
            break
        case _:
            print('\nOpção inválida!')
            print('Tente novamente...\n')
            time.sleep(1.3)
            clear_screen()

# Verifica se o IP é válido
while True:
    clear_screen()
    print_banner()
    target_ip = input('Informe o IP do alvo: ').strip()
    
    if __name__ == '__main__':
        if check_ip(target_ip):
            clear_screen()
            print_banner()
            break
        else:
            print('\nEndereço IP inválido!')
            print('Tente novamente...\n')
            time.sleep(1.3)

# Solicita o caminho da wordlist de usuários
while True:
    wordlist_users = input('Informe o caminho da wordlist de usuários: ').strip()
    
    os.path.abspath(wordlist_users)
    if directory_exists(wordlist_users):
        break
    else:
        print('\nDiretório não encontrado!')
        print('Tente novamente...\n')
        time.sleep(1.3)

# Solicita o caminho da wordlist de senhas
while True:
    wordlist_passwords = input('Informe o caminho da wordlist de senhas: ').strip()
    if directory_exists(wordlist_passwords):
        break
    else:
        print('\nDiretório não encontrado!')
        print('Tente novamente...\n')
        time.sleep(1.3)

clear_screen()
print_banner()

if input(f'{colors["bold"]}{colors["red"]}Deseja iniciar o ataque? (s/n): {colors["red"]}{colors["bold"]}').strip() == 's':
    clear_screen()
    print_banner()
    
    print('INICIANDO ATAQUE...')
    print(f'Alvo: {target_ip}\n')
    time.sleep(1.3)

    if protocol_name in ['ssh', 'telnet', 'ftp']:
        os.system(f'hydra -L {wordlist_users} -P {wordlist_passwords} -t 6 -s {port} -o resultado.txt {protocol_name}://{target_ip}')
        print()
        print(f'{colors["bold"]}{colors["green"]}Ataque finalizado!{colors["green"]}{colors["bold"]}')
        print('Resultado salvo em: resultado.txt')
    else:
        os.system(f'hydra -L {wordlist_users} -P {wordlist_passwords} -t 6 -s {port} -o resultado.txt {target_ip} {protocol_name}-get')
        print()
        print(f'{colors["bold"]}{colors["green"]}Ataque finalizado!{colors["green"]}{colors["bold"]}')
        print('Resultado salvo em: resultado.txt')
else:
    print('Ataque cancelado!\n')