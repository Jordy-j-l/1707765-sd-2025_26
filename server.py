# ==================================================
# IMPORTS
# ==================================================
from xmlrpc.server import SimpleXMLRPCServer


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


# ==================================================
# VALIDAÇÃO DO ENDEREÇO ETHEREUM
# ==================================================
# Função para verificar se o endereço:
# - começa por "0x"
# - tem 42 caracteres
# - está bem formado


# ==================================================
# CONSULTA DO SALDO NA ETHEREUM
# ==================================================
# Função que recebe um endereço Ethereum
# Consulta o saldo no provider Ethereum
# Converte o saldo de wei para ether
# Devolve o saldo ao servidor RPC


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
    return "pong"


def obterSaldo(endereco):
    print(f"[LOG] O endereço {endereco} foi solicitado.", flush=True)
    return f"Endereço recebido: {endereco}"

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