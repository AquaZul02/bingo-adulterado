import random
import time

# Cria tabelas como sets para facilitar remoção e busca
tabelabingo1 = set(random.sample(range(1, 76), 25))
tabelabingo2 = set(random.sample(range(1, 76), 25))
tabelabingo3 = set(random.sample(range(1, 76), 25))
tabelabingo4 = set(random.sample(range(1, 76), 25))
tabelas = [tabelabingo1, tabelabingo2, tabelabingo3, tabelabingo4]

escolha = input("Quantas tabelas você quer que ganhe? (1-4): ")
while escolha not in ['1', '2', '3', '4']:
    escolha = input("Por favor, escolha um número entre 1 e 4: ")
escolha = int(escolha)
if escolha==1:
    tabelaescolhida = tabelabingo1
elif escolha==2:
    tabelaescolhida = tabelabingo2
elif escolha==3:
    tabelaescolhida = tabelabingo3
else:
    tabelaescolhida = tabelabingo4

numeros_sorteados = set()
bingoacabou = False

def conta_numeros(tabela):
    return len(tabela)

while not bingoacabou:
    # Sorteia um número que ainda não saiu
    possiveis = set(range(1, 76)) - numeros_sorteados
    if not possiveis:
        print("Todos os números foram sorteados!")
        break
    sorteio = random.choice(list(tabelaescolhida - numeros_sorteados))
    numeros_sorteados.add(sorteio)
    print(f'Número sorteado: {sorteio}')

    for i, tabela in enumerate(tabelas, 1):
        if sorteio in tabela:
            tabela.remove(sorteio)
            print(f"Número {sorteio} removido da tabela {i}")

    for i, tabela in enumerate(tabelas, 1):
        print(f'Números restantes na tabela {i}: {conta_numeros(tabela)}')

    # Verifica se alguém fez bingo
    for i, tabela in enumerate(tabelas, 1):
        if len(tabela) == 0:
            print(f'Bingo! A tabela {i} completou!')
            bingoacabou = True
            break

    time.sleep(1)  # Pausa para visualizar o sorteio