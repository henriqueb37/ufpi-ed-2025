from typing import Iterable
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np

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
                return
            while atual.next is not None:
                if atual.next.value == value:
                    atual.next = atual.next.next
                    return
                atual = atual.next
        raise KeyError(value)

    def sizes(self) -> list[int]:
        szs = [0] * self.M
        for i in range(self.M):
            atual = self.table[i]
            while atual is not None:
                szs[i] += 1
                atual = atual.next
        return szs

def hash_letra(key: str):
    return ord(key[0] if len(key) > 0 else 'A') - ord('A')

def to_hist(l: Iterable[int]):
    l2 = []
    for i, q in enumerate(l):
        l2.extend([i] * q)
    return l2

def ler_arquivo():
    linhas = None
    with open("alunosED_2025.txt", 'r', encoding='utf-8') as f:
        linhas = [l.strip() for l in f.readlines()]
    return linhas


alunos = ler_arquivo()

def testa_hash(m: int, hashfunc = None):
    ht = HashTable(m, hashfunc)

    for a in alunos:
        ht.add(a)

    media = ht.n / ht.M
    sizes = np.array(ht.sizes())

    _, ax = plt.subplots()

    dm = np.mean(np.abs(sizes - media))
    dp = np.std(sizes)

    print(ht.sizes())
    szs = to_hist(sizes)
    bins = range(0, ht.M + 1)
    ax.hist(szs, bins=bins)
    ax.axhline(y=media, color='r', label='Média')
    ax.set_xticks(np.arange(0, ht.M, 1))
    ax.set_xlabel("Índice")
    ax.set_ylabel("Quantidade")
    ax.set_title(f"Distribuição de dados em tabela hash com M = {m}")
    extra_text_handle = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    ax.legend([extra_text_handle, plt.gca().lines[0]], [f'Desvio Médio = {dm}\nDesvio Padrão = {dp}', 'Média'])

    plt.show()

# testa_hash(26, hash_letra)
# testa_hash(26, hash)
testa_hash(17)
# testa_hash(43)
# testa_hash(97)
# testa_hash(16)
# testa_hash(40)
# testa_hash(100)
