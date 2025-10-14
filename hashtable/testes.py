import unittest
from main import HashTable, hash_letra

class TestesHashTable(unittest.TestCase):
    def teste_adicionar_e_verificar(self):
        ht = HashTable(26, hash_letra)
        l = ['batata', 'cenoura', 'brócolis', 'alcaçúz']
        self.assertEqual(0, ht.n)
        for s in l:
            self.assertFalse(ht.contains(s))
        for s in l:
            ht.add(s)
        for s in l:
            self.assertTrue(ht.contains(s))
        self.assertEqual(4, ht.n)
        l2 = ['abacaxi', 'banana', 'CEREJA', 'durian', 'batata']
        for s in l2[:-1]:
            self.assertFalse(ht.contains(s))
        for s in l2:
            ht.add(s)
        for s in l2:
            self.assertTrue(ht.contains(s))
        self.assertEqual(8, ht.n)
        esperado = [0] * 26
        esperado[0] = 2 # A
        esperado[1] = 3 # B
        esperado[2] = 2 # C
        esperado[3] = 1 # D
        sizes = ht.sizes()
        for i, n in enumerate(sizes):
            self.assertEqual(esperado[i], n)

    def teste_deletar(self):
        ht = HashTable(26, hash_letra)
        for s in ['araucária', 'bambu', 'cana-de-açucar', 'damasqueiro', 'baobá', 'babosa']:
            ht.add(s)

        self.assertEqual(6, ht.n)
        esperado = [0] * 26
        esperado[0] = 1 # A
        esperado[1] = 3 # B
        esperado[2] = 1 # C
        esperado[3] = 1 # D
        sizes = ht.sizes()
        for i, n in enumerate(sizes):
            self.assertEqual(esperado[i], n)

        ht.delete('bambu')
        self.assertTrue(ht.contains('baobá'))
        self.assertTrue(ht.contains('babosa'))
        self.assertFalse(ht.contains('bambu'))

        ht.delete('babosa')
        self.assertTrue(ht.contains('baobá'))
        self.assertFalse(ht.contains('babosa'))

        ht.delete('baobá')
        self.assertFalse(ht.contains('baobá'))

        ht.delete('araucária')
        self.assertFalse(ht.contains('araucária'))

        self.assertRaises(KeyError, ht.delete, 'espada de são jorge')
        self.assertRaises(KeyError, ht.delete, 'babosa')

        self.assertEqual(2, ht.n)
        esperado = [0] * 26
        esperado[0] = 0 # A
        esperado[1] = 0 # B
        esperado[2] = 1 # C
        esperado[3] = 1 # D
        sizes = ht.sizes()
        for i, n in enumerate(sizes):
            self.assertEqual(esperado[i], n)


if __name__ == '__main__':
    unittest.main()
