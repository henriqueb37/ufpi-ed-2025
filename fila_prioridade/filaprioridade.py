from copy import copy
from typing import override


class Node:
    def __init__(self, tipo: str, senha: str):
        self.senha: str = senha
        self.tipo: str = tipo
        self.proximo: Node | None = None


class Fila:
    def __init__(self):
        self._inicio: Node | None = None
        self._fim: Node | None = None
        self._size: int = 0

    def add(self, novo: Node):
        if self._inicio == None:
            self._inicio = novo
            self._fim = novo
        elif self._fim != None:
            self._fim.proximo = novo
            self._fim = novo
        self._size += 1

    def get(self, remove: bool = True):
        tmp = self._inicio
        if remove:
            if self._inicio is self._fim:
                self._inicio = None
                self._fim = None
            if self._inicio != None:
                self._inicio = self._inicio.proximo
            if tmp != None:
                self._size -= 1
        return tmp

    def is_empty(self):
        return self._inicio == None

    def at(self, i: int) -> Node | None:
        if i >= self._size:
            raise IndexError
        cont = 0
        atual = self._inicio
        while atual != None and atual.proximo != None and cont <= i:
            atual = atual.proximo
            cont += 1
        return atual

    def __len__(self):
        return self._size

    @override
    def __str__(self):
        resultado = '['
        atual = self._inicio
        while atual != None:
            resultado += f'{atual.senha} ({atual.tipo}) -> '
            atual = atual.proximo
        resultado += ']'
        return resultado


class Politica:
    def __init__(self, politica: list[tuple[str, int]]):
        self._politica: list[tuple[str, int]] = politica
        self._prioridades: dict[str, int] = {}
        self._max_consecutivos: dict[str, int] = {}
        for i, (tipo, max_consec) in enumerate(politica):
            self._prioridades[tipo] = len(politica) - i
            self._max_consecutivos[tipo] = max_consec

    def get_prioridade(self, tipo: str):
        return self._prioridades[tipo]

    def get_max_consecutivo(self, tipo: str):
        return self._max_consecutivos[tipo]

    def __iter__(self):
        for t, m in self._politica:
            yield t, m


class FilaPrioridade:
    def __init__(self):
        # [(tipo, máximo consecutivo)]
        self._politica: Politica = Politica([('P', 1), ('N', 2)])
        self._filas: dict[str, Fila] = {}
        self._saidas: dict[str, int] = {}
        for tipo, _ in self._politica:
            self._filas[tipo] = Fila()
            self._saidas[tipo] = 0
        self._size: int = 0
        self._ultima_saida: str | None = None

    def add(
        self,
        senha: str | None = None,
        tipo: str | None = None,
        batch: list[tuple[str, str]] | None = None,
    ):
        if tipo == None or senha == None:
            if batch == None:
                raise ValueError('batch ou tipo e senha são necessários para adicionar')
            else:
                for t, s in batch:
                    self.add(t, s)
                return
        self._filas[tipo].add(Node(tipo, senha))
        self._size += 1

    def get(self, debug: bool = False) -> tuple[str, str] | None:
        # (senha, tipo)
        retorno = None
        # Percorre _política até achar um que não tenha atingido o limite
        for tipo, max_consec in self._politica:
            if debug:
                print(f'{tipo}: {self._filas[tipo]}')
            if self._saidas[tipo] < max_consec and retorno == None:
                node = self._filas[tipo].get()
                if node != None:
                    if debug:
                        print(f'Retirando {node.senha} ({node.tipo})')
                    self._saidas[tipo] += 1
                    retorno = node.senha, node.tipo
                    break
        # Se não achar nenhum que não tenha atingido o limite, pega o primeiro disponível.
        # De acordo com a preferência da ordem definida em _política
        if retorno == None:
            for tipo, _ in self._politica:
                fila = self._filas[tipo]
                node = fila.get()
                if node != None:
                    retorno = node.senha, node.tipo
                    self._saidas[tipo] += 1
                    break
        if retorno != None:
            self._size -= 1
            # Se o retirado agora tiver uma prioridade maior que o retirado anteriormente,
            # significa que a lista já retirou todos os de menor prioridade disponível,
            # Então a contagem deve ser reiniciada
            if self._ultima_saida != None and self._politica.get_prioridade(
                retorno[1]
            ) > self._politica.get_prioridade(self._ultima_saida):
                for tipo in self._saidas:
                    self._saidas[tipo] = 0
                self._saidas[retorno[1]] += 1
            self._ultima_saida = retorno[1]

        return retorno

    def __iter__(self):
        # Cria uma nova fila para simular a saídas dessa
        copia = copy(self)
        copia._saidas = self._saidas.copy()
        # De novo o copy, mas, dessa vez, mantém os Nodes originais porquê é uma cópia
        # "rasa" então não cria objetos novos para cada uma das filas.
        # Então é pra ser mais eficiente que uma cópia profunda
        copia._filas = {k: copy(v) for k, v in self._filas.items()}

        # Retira os items da cópia
        atual = copia.get()
        # Vai adicionando enquanto sobrar objetos nas filas
        while atual != None:
            yield atual
            atual = copia.get()

    def __len__(self):
        return self._size

    def count(self, tipo: str):
        return len(self._filas[tipo])
