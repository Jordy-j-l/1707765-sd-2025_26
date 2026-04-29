# ==================================================
# IMPORTS
# ==================================================
from xmlrpc.client import ServerProxy


# ==================================================
# CONFIGURAÇÕES DO CLIENTE RPC
# ==================================================
# URL do servidor RPC
SERVER_URL = "http://localhost:8000"
def config():
    client = ServerProxy(SERVER_URL)
    response = client.ping()
    print("Resposta do servidor:", response)
    return client
    



# ==================================================
# CHAMADA RPC AO SERVIDOR/# APRESENTAR RESULTADO

# ==================================================
# O cliente chama a função remota:
# obterSaldo(endereco)


    

# Mostrar no ecrã:
# - endereço consultado
# - saldo recebido
# - mensagem de erro, se existir

def Show(endereco):
    client=config()
    try:
        resposta = client.obterSaldo(endereco)

        print()
        print("############### RESULTADO ##################")
        print(f"Conta: {endereco}")
        print(f"Resposta: {resposta}")
        print("############################################")
    except Exception as erro:
        print()
        print("################ ERRO ######################")
        print("Não foi possível contactar o servidor RPC.")
        print(f"Detalhe: {erro}")
        print("############################################")

# ==================================================
# PEDIR ENDEREÇO AO UTILIZADOR/MAIN
# ==================================================
# O utilizador escreve o endereço Ethereum
def menu():
    print()
    print("############################################")
    print("#           ETHEREUM ACCOUNT                #")
    print("#                 /\\                       #")
    print("#                /  \\                      #")
    print("#               /____\\                     #")
    print("#               \\    /                     #")
    print("#                \\  /                      #")
    print("#                 \\/                       #")
    print("############################################")
    print()
def main():
    
    menu()
    endereco=input("INSIRA A CONTA DESEJADA =>")
    print("############################################")
    print("A enviar pedido ao servidor RPC...")
    print("############################################")
    Show(endereco)
if __name__ == "__main__":
    main()