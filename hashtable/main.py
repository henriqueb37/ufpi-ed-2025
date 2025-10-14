import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from typing import Any, Callable, Iterable, cast
from matplotlib.patches import Polygon, Rectangle
from numpy.typing import NDArray

# Forçar seed da função hash como sendo 0
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)

class Node:
    def __init__(self, value: str):
        self.value: str = value
        self.next: Node | None = None

class HashTable:
    def __init__(self, M: int, hashfunc = None):
        self.M = M
        self.n = 0
        self.hashfunc = (lambda x: hashfunc(x) % self.M) if hashfunc is not None else self._hash
        self.table: list[Node | None] = [None] * M

    def _hash(self, key: str):
        h = 0
        for c in key:
            h = (31 * h + ord(c)) % self.M
        return h

    def add(self, value: str):
        if len(value) < 1:
            return
        novo = Node(value)
        h = self.hashfunc(value)
        if self.table[h] is None:
            self.table[h] = novo
            self.n += 1
            return
        atual = self.table[h]
        assert atual is not None
        while atual.next is not None:
            if atual.value == value:
                return
            atual = atual.next
        atual.next = novo
        self.n += 1

    def delete(self, value):
        for i in range(self.M):
            atual = self.table[i]
            if atual is None:
                continue
            if atual.value == value:
                self.table[i] = atual.next
                self.n -= 1
                return
            while atual.next is not None:
                if atual.next.value == value:
                    atual.next = atual.next.next
                    self.n -= 1
                    return
                atual = atual.next
        raise KeyError(value)

    def contains(self, value) -> bool:
        for i in range(self.M):
            atual = self.table[i]
            while atual is not None:
                if atual.value == value:
                    return True
                atual = atual.next
        return False

    def sizes(self) -> list[int]:
        szs = [0] * self.M
        for i in range(self.M):
            atual = self.table[i]
            while atual is not None:
                szs[i] += 1
                atual = atual.next
        return szs

def hash_letra(key: str):
    return ord(key[0].upper() if len(key) > 0 else 'A') - ord('A')

def to_hist(l: Iterable[int]):
    l2 = []
    for i, q in enumerate(l):
        l2.extend([i] * q)
    return l2

def ler_arquivo():
    linhas = None
    with open("alunosED_2025.txt", 'r', encoding='utf-8') as f:
        linhas = [l.strip().upper() for l in f.readlines()]
    return linhas


alunos = ler_arquivo()

def mostra_grafico(sizes: NDArray[Any]):
    _, ax = plt.subplots()

    n = sum(sizes)
    m = len(sizes)
    media = n / m
    szs = to_hist(sizes)
    bins = range(0, m + 1)

    dm = np.mean(np.abs(sizes - media))
    dp = np.std(sizes)

    _, _, patches = ax.hist(szs, bins=bins)
    for p, s in zip(cast(list[Polygon], patches), sizes):
        if s/n > 0.1:
            p.set_facecolor('red')
            # print(f'{s} > 10% de {n}')
        else:
            p.set_facecolor('blue')

    ax.axhline(y=media, color='r', label='Média')
    ax.set_xticks(np.arange(0, m, 1))
    ax.set_xlabel("Índice")
    ax.set_ylabel("Quantidade")
    ax.set_title(f"Distribuição de dados em tabela hash com M = {m}")
    extra_text_handle = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    ax.legend([extra_text_handle, plt.gca().lines[0]], [f'Desvio Médio = {dm}\nDesvio Padrão = {dp}', 'Média'])

    plt.show()

def testa_hash(m: int, hashfunc = None, grafico = False):
    ht = HashTable(m, hashfunc)

    for a in alunos:
        ht.add(a)

    sizes = np.array(ht.sizes())

    # print(ht.sizes())
    if grafico:
        mostra_grafico(sizes)

    dp = np.std(sizes)


    return cast(float, dp)

def get_res(menu: list[tuple[str, Callable[[], Any]]]):
    while True:
        for i, f in enumerate(menu):
            print(f'{i+1}. {f[0]}')
        print(f'{len(menu) + 1}. Cancelar')
        res = input('Digite a opção desejada: ').strip()
        try:
            r = int(res)
            if r < 1:
                raise Exception()
            if r == len(menu) + 1:
                return None
            return menu[r - 1][1]()
        except Exception:
            print(f'Opção {res} inválida!')

def main():
    tabelas: list[tuple[str, tuple[int] | tuple[int, Callable[[Any], int] | None]]] = [
        ("Primeira letra",          (26, hash_letra)),
        ("Função nativa",           (26, hash)),
        ("Função da sala, M = 17",  (17,)),
        ("Função da sala, M = 43",  (43,)),
        ("Função da sala, M = 97",  (97,)),
        ("Função da sala, M = 16",  (16,)),
        ("Função da sala, M = 40",  (40,)),
        ("Função da sala, M = 100", (100,)),
    ]

    def gerar_graficos(tabelas):
        for desc, tab in tabelas:
            print(f'Gerando gráfico "{desc}"...')
            testa_hash(*tab, grafico=True)

    def compara_desvios(tabelas):
        dps = [(x[0], float(testa_hash(*x[1]))) for x in tabelas]
        print('Lista dos menores desvios padrão:')
        max_text = max([len(x[0]) for x in tabelas])
        print('\n'.join([f'{x[0]:{max_text}}: {x[1]}' for x in sorted(dps, key=lambda x: x[1])]))

    menu = [
        ('Gerar gráficos', lambda: gerar_graficos(tabelas)),
        ('Ranquear distribuições', lambda: compara_desvios(tabelas)),
    ]

    while True:
        res = get_res(menu)
        if res is None:
            break

if __name__ == '__main__':
    main()
