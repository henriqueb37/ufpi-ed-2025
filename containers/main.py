import matplotlib.pyplot as plt
from re import split
from wrappers import *
from symbtree import time_to_add, time_to_remove, time_to_search

NOME_ARQUIVO = './leipzig100k.txt'
PALAVRAS_ESCOLHIDAS = ["Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"]
N_TESTES = 1

def teste_containers_add(palavras):
    tempos: dict[str, float] = {}
    for t in CONTAINER_TYPES:
        tempos[t.name] = sum(time_to_add(palavras, t) for _ in range(N_TESTES)) / N_TESTES
    return tempos

def teste_containers_search(palavras, to_search):
    tempos = {}
    for t in CONTAINER_TYPES:
        tempos[t.name] = sum(time_to_search(palavras, to_search, t) for _ in range(N_TESTES)) / N_TESTES
    return tempos

def teste_containers_remove(palavras, to_remove):
    tempos = {}
    for t in CONTAINER_TYPES:
        tempos[t.name] = sum(time_to_remove(palavras, to_remove, t) for _ in range(N_TESTES)) / N_TESTES
    return tempos

def mostrar_grafico(dados, title):
    d = dict(sorted(dados.items(), key=lambda x: x[1]))
    b = plt.bar(list(d.keys()), list(d.values()))
    plt.bar_label(b, fmt=lambda x: f"{x:.2e}")
    plt.xticks(rotation=20, ha='right')
    plt.xlabel('Container')
    plt.ylabel('Tempo de execução em segundos')
    plt.title(title)
    plt.show()

def carregar_palavras():
    with open(NOME_ARQUIVO, 'r') as f:
        palavras = split(r'[^a-zA-ZÀ-ÖØ-öø-ÿ]+', f.read())
    return palavras

def main():
    try:
        print("Carregando palavras...")
        palavras = carregar_palavras()
        print(f"{len(palavras)} palavras carregadas.")
        palavras = list(set(palavras))
        print(f"{len(palavras)} palavras não repetidas.")
    except:
        print('Erro ao ler o arquivo ', NOME_ARQUIVO)
        exit(1)
    print('\n=== Adição ===')
    a = teste_containers_add(palavras)
    mostrar_grafico(a, "Adição de palavras")
    print('\n=== Procura ===')
    p = teste_containers_search(palavras, PALAVRAS_ESCOLHIDAS)
    mostrar_grafico(p, "Busca de palavras")
    print('\n=== Remoção ===')
    r = teste_containers_remove(palavras, PALAVRAS_ESCOLHIDAS)
    mostrar_grafico(r, "Remoção de palavras")


if __name__ == '__main__':
    main()
