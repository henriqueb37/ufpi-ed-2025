# dict, list, set, tuple
# namedtuple, deque, ChainMap
# Counter, OrderedDict, defaultDict
# UserDict, UserList, UserString

from abc import ABC, abstractmethod
from collections import (
    deque, ChainMap, Counter, OrderedDict, 
    defaultdict, UserDict, UserList, UserString, namedtuple
)


class ContainerWrapper(ABC):
    # Definido como anotação de tipo aqui, mas implementado nas subclasses
    name: str

    @abstractmethod
    def add(self, value: str):
        pass

    @abstractmethod
    def find(self, value: str) -> bool:
        pass

    @abstractmethod
    def remove(self, value: str):
        pass

class ListWrapper(ContainerWrapper):
    """Wrapper para a 'list' nativa."""
    name = "list"

    def __init__(self):
        self.data = []

    def add(self, value: str):
        self.data.append(value)

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        try:
            self.data.remove(value)
        except ValueError:
            pass

class DequeWrapper(ContainerWrapper):
    """Wrapper para 'collections.deque'."""
    name = "deque"

    def __init__(self):
        self.data = deque()

    def add(self, value: str):
        self.data.append(value)

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        try:
            self.data.remove(value)
        except ValueError:
            pass

class UserListWrapper(ContainerWrapper):
    """Wrapper para 'collections.UserList'."""
    name = "UserList"

    def __init__(self):
        self.data = UserList()

    def add(self, value: str):
        self.data.append(value)

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        try:
            self.data.remove(value)
        except ValueError:
            pass

class TupleWrapper(ContainerWrapper):
    """Wrapper para 'tuple' (demonstra ineficiência de imutabilidade)."""
    name = "tuple"

    def __init__(self):
        self.data = ()

    def add(self, value: str):
        self.data = self.data + (value,)

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        try:
            idx = self.data.index(value)
            self.data = self.data[:idx] + self.data[idx+1:]
        except ValueError:
            pass

class NamedTupleWrapper(ContainerWrapper):
    name = "namedtuple"

    def __init__(self):
        self.TupleType = namedtuple("Container", [])
        self.data = self.TupleType()

    def _rebuild(self, items_list):
        field_names = [f"f{i}" for i in range(len(items_list))]
        self.TupleType = namedtuple("Container", field_names)
        self.data = self.TupleType(*items_list)

    def add(self, value: str):
        current_items: list[str] = list(self.data)
        current_items.append(value)
        self._rebuild(current_items)

    def find(self, value: str) -> bool:
        # Busca nativa (O(n))
        return value in self.data

    def remove(self, value: str):
        if value in self.data:
            current_items: list[str] = list(self.data)
            current_items.remove(value)
            self._rebuild(current_items)

class SetWrapper(ContainerWrapper):
    """Wrapper para o 'set' nativo."""
    name = "set"

    def __init__(self):
        self.data = set()

    def add(self, value: str):
        self.data.add(value)

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        self.data.discard(value)

class DictWrapper(ContainerWrapper):
    """Wrapper para o 'dict' nativo."""
    name = "dict"

    def __init__(self):
        self.data = {}

    def add(self, value: str):
        self.data[value] = None

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        self.data.pop(value, None)

class OrderedDictWrapper(ContainerWrapper):
    """Wrapper para 'collections.OrderedDict'."""
    name = "OrderedDict"

    def __init__(self):
        self.data = OrderedDict()

    def add(self, value: str):
        self.data[value] = None

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        self.data.pop(value, None)

class DefaultDictWrapper(ContainerWrapper):
    """Wrapper para 'collections.defaultdict'."""
    name = "defaultdict"

    def __init__(self):
        self.data = defaultdict(lambda: None)

    def add(self, value: str):
        self.data[value] = None

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        self.data.pop(value, None)

class CounterWrapper(ContainerWrapper):
    """Wrapper para 'collections.Counter'."""
    name = "Counter"

    def __init__(self):
        self.data = Counter()

    def add(self, value: str):
        self.data[value] += 1

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        self.data.pop(value, None)

class ChainMapWrapper(ContainerWrapper):
    """Wrapper para 'collections.ChainMap'."""
    name = "ChainMap"

    def __init__(self):
        self.map_principal = {}
        self.data = ChainMap(self.map_principal)

    def add(self, value: str):
        self.data[value] = None

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        self.data.pop(value, None)

class UserDictWrapper(ContainerWrapper):
    """Wrapper para 'collections.UserDict'."""
    name = "UserDict"

    def __init__(self):
        self.data = UserDict()

    def add(self, value: str):
        self.data[value] = None

    def find(self, value: str) -> bool:
        return value in self.data

    def remove(self, value: str):
        self.data.pop(value, None)

class UserStringWrapper(ContainerWrapper):
    """Wrapper para 'collections.UserString'."""
    name = "UserString"

    def __init__(self):
        self.data = UserString("|")

    def add(self, value: str):
        self.data = self.data + value + "|"

    def find(self, value: str) -> bool:
        return f"|{value}|" in self.data

    def remove(self, value: str):
        try:
            idx = self.data.index(f"|{value}|")
            self.data = self.data[:idx+1] + self.data[idx + len(value) + 2:]
        except:
            pass

CONTAINER_TYPES: list[type[ContainerWrapper]] = [
    DictWrapper,
    ListWrapper,
    SetWrapper,
    TupleWrapper,
    # NamedTupleWrapper,
    DequeWrapper,
    ChainMapWrapper,
    CounterWrapper,
    OrderedDictWrapper,
    DefaultDictWrapper,
    UserDictWrapper,
    UserListWrapper,
    UserStringWrapper
]
