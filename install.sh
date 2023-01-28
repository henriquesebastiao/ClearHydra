VERMELHO='\033[0;31m'
AZUL='\033[0;34m'
VERDE='\033[0;32m'
BRANCO='\033[0m'

# Função para verificar se o usuário é root
checkroot(){
    SAVE_LD_PRELOAD="$LD_PRELOAD"
    unset LD_PRELOAD
    if [ "$(id -u)" -ne 0 ]; then
        echo -e "${VERMELHO}Você deve ser o usuário root para executar este script!\n${BRANCO}"
        exit 1
    else
        # Se o usuário for root, execute a função install
        apt update
        apt install hydra, python3 -y
        if [ "$?" -ne 0 ]; then
        echo -e "${VERMELHO}Um erro ocorreu! Parece que o apt não funciona.\n${BRANCO}"
        exit 1
        fi
    fi
}

checkroot