# ==================================================
# IMPORTS
# ==================================================
from xmlrpc.server import SimpleXMLRPCServer
import requests

# ==================================================
# CONFIGURAÇÕES DO SERVIDOR RPC
# ==================================================
HOST = "localhost"
PORT = 8000


# ==================================================
# CONFIGURAÇÕES DO ETHEREUM PROVIDER
# ==================================================
# URL do provider Ethereum / nó Ethereum
# Exemplo: INFURA_URL, ALCHEMY_URL ou outro endpoint
ETHERSCAN_API_KEY = "U7TZYZRAFB3KZHUU5TXYWRS9YY8A3Z3FMI"
ETHERSCAN_URL = "https://api.etherscan.io/v2/api"


# ==================================================
# VALIDAÇÃO DO ENDEREÇO ETHEREUM
# ==================================================
# Função para verificar se o endereço:
# - começa por "0x"
# - tem 42 caracteres
# - está bem formado
def valEndereco(endereco):

    if not endereco.startswith("0x"):
        return False
    if len(endereco) != 42:
        return False
    hex_chars = "0123456789abcdefABCDEF"
    for c in endereco[2:]:
        if c not in hex_chars:
            return False
    return True
# ==================================================
# CONSULTA DO SALDO NA ETHEREUM
# ==================================================
# Função que recebe um endereço Ethereum
# Consulta o saldo no provider Ethereum
# Converte o saldo de wei para ether
# Devolve o saldo ao servidor RPC

def consultarSaldoEthereum(endereco):
    parametros = {
        "chainid": "1",
        "module": "account",
        "action": "balance",
        "address": endereco,
        "tag": "latest",
        "apikey": ETHERSCAN_API_KEY
    }
    resposta = requests.get(ETHERSCAN_URL, params=parametros)
    dados = resposta.json()
    if dados["status"] != "1":
        return "Erro ao consultar saldo"
    saldo_wei= int(dados["result"])
    saldo=saldo_wei / 10**18 #saldo em ether
    return str(saldo)

# ==================================================
# FUNÇÃO RPC DISPONÍVEL PARA O CLIENTE
# ==================================================
# Função obterSaldo(endereco)
# Esta é a função que o cliente vai chamar remotamente
# Passos:
# 1. Receber endereço
# 2. Validar endereço
# 3. Consultar saldo
# 4. Devolver resultado

def ping():
    return "Ligação estabelecido com sucesso"


def obterSaldo(endereco):
    
    print(f"[LOG] O endereço {endereco} foi solicitado.", flush=True)
    if not valEndereco(endereco):
        print("Endereço invalido")
        return False
    saldo=consultarSaldoEthereum(endereco)

    return f"Saldo da Conta: {saldo} ETH"

# ==================================================
# CRIAÇÃO DO SERVIDOR RPC
# ==================================================
# Criar servidor SimpleXMLRPCServer
# Registar a função obterSaldo
# Mostrar mensagem "Servidor RPC ativo"
# Manter servidor em execução

server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)

server.register_function(ping, "ping")
server.register_function(obterSaldo, "obterSaldo")

print(f"Servidor RPC ativo em http://{HOST}:{PORT}", flush=True)

server.serve_forever()