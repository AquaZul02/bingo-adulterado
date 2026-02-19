import random
import time

tabelabingo1 = set(random.sample(range(1, 76), 25))
tabelabingo2 = set(random.sample(range(1, 76), 25))
tabelabingo3 = set(random.sample(range(1, 76), 25))
tabelabingo4 = set(random.sample(range(1, 76), 25))
tabelas = [tabelabingo1, tabelabingo2, tabelabingo3, tabelabingo4]

numeros_sorteados = set()
bingoacabou = False

def conta_numeros(tabela):
    return len(tabela)

while not bingoacabou:
    possiveis = set(range(1, 76)) - numeros_sorteados
    if not possiveis:
        print("Todos os números foram sorteados!")
        break
    sorteio = random.choice(list(possiveis))
    numeros_sorteados.add(sorteio)
    print(f'Número sorteado: {sorteio}')

    for i, tabela in enumerate(tabelas, 1):
        if sorteio in tabela:
            tabela.remove(sorteio)
            print(f"Número {sorteio} removido da tabela {i}")

    for i, tabela in enumerate(tabelas, 1):
        print(f'Números restantes na tabela {i}: {conta_numeros(tabela)}')

    for i, tabela in enumerate(tabelas, 1):
        if len(tabela) == 0:
            print(f'Bingo! A tabela {i} completou!')
            bingoacabou = True
            break

    time.sleep(1)