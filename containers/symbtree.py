from time import perf_counter
from wrappers import ContainerWrapper


class HashTab:
    def __init__(self, container_type: type[ContainerWrapper], m: int):
        self.container_type = container_type
        self.m = m
        self.arr = [container_type() for _ in range(m)]

    def _hash(self, value: str):
        return hash(value) % self.m

    def add(self, value: str):
        h = self._hash(value)
        self.arr[h].add(value)

    def find(self, value: str):
        h = self._hash(value)
        return self.arr[h].find(value)

    def remove(self, value: str):
        h = self._hash(value)
        self.arr[h].remove(value)

def time_to_add(palavras: list[str], container_type: type[ContainerWrapper], m=97) -> float:
    st = HashTab(container_type, m=m)
    tempo = 0
    for p in palavras:
        start = perf_counter()
        st.add(p)
        end = perf_counter()
        tempo += end - start
    return tempo

def time_to_search(palavras: list[str], to_search: list[str], container_type: type[ContainerWrapper], m=97) -> float:
    st = HashTab(container_type, m=m)
    tempo = 0
    for p in palavras:
        st.add(p)
    for p in to_search:
        start = perf_counter()
        st.find(p)
        end = perf_counter()
        tempo += end - start
    return tempo

def time_to_remove(palavras: list[str], to_remove: list[str], container_type: type[ContainerWrapper], m=97) -> float:
    st = HashTab(container_type, m=m)
    tempo = 0
    for p in palavras:
        st.add(p)
    for p in to_remove:
        start = perf_counter()
        st.remove(p)
        end = perf_counter()
        tempo += end - start
    return tempo
