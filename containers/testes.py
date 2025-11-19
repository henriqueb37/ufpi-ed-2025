import uuid
import random
from wrappers import *

NUM_SYMBOLS = 500

def generate_test_data(n, label):
    """Gera 'n' símbolos UUID únicos."""
    print(f"Gerando {n} símbolos para '{label}'...")
    return [str(uuid.uuid4()) for _ in range(n)]

def run_test(wrapper_class, symbols_add, symbols_find_success, symbols_find_fail, symbols_remove):
    """Executa o ciclo de vida completo (add, find, remove) para um wrapper."""
    container = wrapper_class()
    results = {}
    print(f"=== {wrapper_class.__name__} ===")

    # --- Teste ADD ---
    print('Adicionando...')
    for symbol in symbols_add:
        container.add(symbol)

    # --- Teste FIND (Success / Hit) ---
    print('Procurando...')
    for symbol in symbols_find_success:
        r = container.find(symbol)
        if not r:
            print(symbol, 'Not found!')
        assert r

    # --- Teste FIND (Failure / Miss) ---
    print('Procurando itens inexistentes...')
    for symbol in symbols_find_fail:
        r = container.find(symbol)
        if r:
            print(symbol, 'Found!')
        assert not r

    # --- Teste REMOVE ---
    print('Removendo...')
    for symbol in symbols_remove:
        container.remove(symbol)

    # --- Teste FIND depois de REMOVE (Failure / Miss) ---
    print('Procurando depois de remover...')
    for symbol in symbols_find_fail:
        r = container.find(symbol)
        if r:
            print(symbol, 'Found!')
        assert not r

    return results

def main():
    symbols_add = generate_test_data(NUM_SYMBOLS, "add")
    symbols_find_fail = generate_test_data(NUM_SYMBOLS, "find (miss)")
    
    symbols_find_success = symbols_add[:]
    random.shuffle(symbols_find_success)
    
    symbols_remove = symbols_add[:]
    random.shuffle(symbols_remove)

    for t in CONTAINER_TYPES:
        run_test(t, symbols_add, symbols_find_success, symbols_find_fail, symbols_remove)

if __name__ == "__main__":
    main()
