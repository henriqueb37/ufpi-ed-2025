import unittest
from filaprioridade import FilaPrioridade

def testar_fila(teste: unittest.TestCase, para_adicionar: list[str], esperado: list[tuple[int, str]]):
    fp = FilaPrioridade()
    for i, t in enumerate(para_adicionar):
        fp.add(t, str(i))
    for s, t in esperado:
        node = fp.get()
        teste.assertIsNotNone(node)
        if node:
            teste.assertEqual(str(s), node[0])
            teste.assertEqual(t, node[1])

class TesteFilaPrioridade(unittest.TestCase):
    def testar_add_get(self):
        testar_fila(
            self,
            ['P', 'N', 'N'],
            [(0, 'P'), (1, 'N'), (2, 'N')]
        )
        testar_fila(
            self,
            ['P', 'N', 'N', 'P'],
            [(0, 'P'), (1, 'N'), (2, 'N'), (3, 'P')]
        )
        testar_fila(
            self,
            ['P', 'N', 'N', 'P', 'P'],
            [(0, 'P'), (1, 'N'), (2, 'N'), (3, 'P'), (4, 'P')]
        )
        testar_fila(
            self,
            ['N', 'N', 'P', 'P', 'P'],
            [(2, 'P'), (0, 'N'), (1, 'N'), (3, 'P'), (4, 'P')]
        )
        testar_fila(
            self,
            ['N', 'N', 'N', 'P', 'P', 'P'],
            [(3, 'P'), (0, 'N'), (1, 'N'), (4, 'P'), (2, 'N'), (5, 'P')]
        )
        testar_fila(
            self,
            ['P', 'N', 'P', 'P', 'N'],
            [(0, 'P'), (1, 'N'), (4, 'N'), (2, 'P'), (3, 'P')]
        )
        testar_fila(
            self,
            ['P', 'P', 'N'],
            [(0, 'P'), (2, 'N'), (1, 'P')]
        )
        testar_fila(
            self,
            ['P', 'N', 'N', 'P', 'P', 'N'],
            [(0, 'P'), (1, 'N'), (2, 'N'), (3, 'P'), (5, 'N'), (4, 'P')],
        )
        testar_fila(
            self,
            ['P', 'N', 'P', 'P'],
            [(0, 'P'), (1, 'N'), (2, 'P'), (3, 'P')]
        )
        testar_fila(
            self,
            ['P', 'N', 'N', 'N', 'P'],
            [(0, 'P'), (1, 'N'), (2, 'N'), (4, 'P'), (3, 'N')],
        )

if __name__ == "__main__":
    _ = unittest.main()
