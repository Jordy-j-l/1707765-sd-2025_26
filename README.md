# 1707765-sd-2025_26
Repositorio feito para a disciplina de Sistemas distribuidos
# Obter saldos de contas da Ethereum via RPC

## Objetivo

Este projeto permite consultar o saldo de uma conta Ethereum usando RPC.

O cliente introduz um endereço Ethereum e envia esse endereço ao servidor.
O servidor consulta o saldo através de um Ethereum provider e devolve o resultado ao cliente.

## Ficheiros

- `cliente.py` — programa cliente
- `server.py` — servidor RPC e lógica da consulta Ethereum
- `requirements_1707765.txt` — ordem de execução dos programas
## Fluxo do sistema
Cliente introduz endereço Ethereum.
Cliente chama uma função RPC no servidor.
Servidor valida o endereço.
Servidor consulta o saldo na Ethereum.
Servidor devolve o saldo ao cliente.
Cliente apresenta o saldo.
## Como executar
```bash
#Primeiro executar o servidor:
python server.py
#Depois executar o cliente:
python cliente.py
```  
