import matplotlib.pyplot as plt

tempos = {
    100: {
        'Bubble': 122.013,
        'Selection': 18.376,
        'Insertion': 24.616,
        'Shell': 0.71,
        'Merge': 0.0463,
        'Quick': 0.028,
        'Heap': 0.0434,
    },
    250: {
        'Bubble': 1036.620,
        'Selection': 116.588,
        'Insertion': 156.967,
        'Shell': 0.199,
        'Merge': 0.1234,
        'Quick': 0.0858,
        'Heap': 0.1284,
    },
    500: {
        'Bubble': 3884.64,
        'Selection': 482.667,
        'Insertion': 643.192,
        'Shell': 0.4162,
        'Merge': 0.2576,
        'Quick': 0.2026,
        'Heap': 0.3144,
    }
}

amostras = list(tempos.keys())
if len(amostras) <= 0:
    print('Não há dados disponíveis para gerar os gráficos.')
    exit()

def get_res_amostra():
    while True:
        for i, c in enumerate(amostras):
            print(f'{i + 1}. {c}k')
        print('SAIR: Sair do programa')
        res = input('Qual tamanho de amostra deseja utilizar? ').strip().lower()
        if res == 'sair':
            exit()
        if res in ['1', '2', '3']:
            return amostras[int(res) - 1]
        print('Opção inválida')

def get_res_cats(am):
    categorias = list(tempos[am].keys())
    while True:
        for i, c in enumerate(categorias):
            print(f'{i + 1}. {c}')
        print('SAIR: Sair do programa')
        print('Quais algoritmos deseja utilizar? ')
        res = input('[ex: 2 3 5] ').lower().strip()
        if res == 'sair':
            exit()
        res = res.split()
        res2: list[str] = []
        for r in res:
            try:
                res2.append(categorias[int(r) - 1])
            except:
                print(f'Opção {r} inválida!')
                continue
        return res2







while True:
    amostra = get_res_amostra()
    cats = get_res_cats(amostra)
    vals = [tempos[amostra][c] for c in cats]

    print('\nMostrando gráfico...\n')

    fig, ax = plt.subplots()
    bars = ax.barh(cats[::-1], vals[::-1])
    ax.bar_label(bars, label_type='edge', color='black', fontsize=10)
    ax.set_xlabel('Tempo em segundos (menor é melhor)')
    ax.set_ylabel('Algoritmo')
    ax.set_title(f'nomes{amostra}k.txt')
    plt.show()
    
