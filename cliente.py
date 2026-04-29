# ==================================================
# IMPORTS
# ==================================================
from xmlrpc.client import ServerProxy


# ==================================================
# CONFIGURAÇÕES DO CLIENTE RPC
# ==================================================
# URL do servidor RPC
SERVER_URL = "http://localhost:8000"
client = ServerProxy(SERVER_URL)
response = client.ping()

print("Resposta do servidor:", response)

# ==================================================
# PEDIR ENDEREÇO AO UTILIZADOR
# ==================================================
# O utilizador escreve o endereço Ethereum


# ==================================================
# CHAMADA RPC AO SERVIDOR
# ==================================================
# O cliente chama a função remota:
# obterSaldo(endereco)


# ==================================================
# APRESENTAR RESULTADO
# ==================================================
# Mostrar no ecrã:
# - endereço consultado
# - saldo recebido
# - mensagem de erro, se existir