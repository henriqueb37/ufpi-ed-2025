import tkinter as tk
from tkinter import ttk
from filaprioridade import FilaPrioridade  # pyright: ignore[reportImplicitRelativeImport]
# import sv_ttk


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        self.hist: list[str] = []
        self.fp: FilaPrioridade = FilaPrioridade()
        self.p_cont: int = 0
        self.n_cont: int = 0

        super().__init__()
        self.title('Painel de administrador')
        self.geometry('600x200')
        _ = self.columnconfigure(0, weight=1)
        _ = self.rowconfigure(0, weight=1)

        self.janela_cliente: JanelaCliente | None = None
        # Frame principal
        self.frm: ttk.Frame = ttk.Frame(self, padding=10)
        self.frm.grid(sticky='nsew')
        self.frm.master.maxsize(600, 200)  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
        _ = self.frm.columnconfigure(0)
        _ = self.frm.columnconfigure(1, weight=1)
        _ = self.frm.rowconfigure(0, weight=1)

        # Label que mostra o tamanho da fila
        self.lbl_fila: ttk.Label = ttk.Label(self.frm, text='Vazia', wraplength=300)
        self.lbl_fila.grid(row=0, column=1, rowspan=2)

        # Frame pra deixar os botões centralizados
        frm_botoes = ttk.Frame(self.frm)
        frm_botoes.grid(row=0, column=0)

        btn_addP = ttk.Button(
            frm_botoes, text='Adicionar Prioridade', command=self.add_P
        )
        btn_addP.grid(row=0, column=0)

        btn_addN = ttk.Button(frm_botoes, text='Adicionar Normal', command=self.add_N)
        btn_addN.grid(row=1, column=0)

        btn_atenderCliente = ttk.Button(
            frm_botoes, text='Atender Próximo Cliente', command=self.atender_cliente
        )
        btn_atenderCliente.grid(row=2, column=0)

        btn_openCliente = ttk.Button(
            self.frm, text='Abrir painel de clientes', command=self.abrir_janela_cliente
        )
        btn_openCliente.grid(row=1, column=0)

    def update_lbl_fila(self):
        _ = self.lbl_fila.configure(
            text=(
                ' -> '.join([senha for senha, _ in self.fp])
                if len(self.fp) > 0
                else 'Vazia'
            )
        )

    def add_P(self):
        self.p_cont += 1
        self.fp.add(f'P{self.p_cont}', 'P')
        self.update_lbl_fila()

    def add_N(self):
        self.n_cont += 1
        self.fp.add(f'N{self.n_cont}', 'N')
        self.update_lbl_fila()

    def abrir_janela_cliente(self):
        if self.janela_cliente is None or not self.janela_cliente.winfo_exists():
            self.janela_cliente = JanelaCliente(self, self.hist)
        else:
            self.janela_cliente.open()

    def atender_cliente(self):
        cliente = self.fp.get()
        if self.janela_cliente is not None and cliente is not None:
            self.hist.append(cliente[0])
            self.janela_cliente.reveal(*cliente)
        self.update_lbl_fila()


class JanelaCliente(tk.Toplevel):
    def __init__(self, root: tk.Tk, hist: list[str]):
        self.hist: list[str] = hist[1:] if len(hist) >= 2 else []
        self.senha_atual: str = hist[0] if len(hist) >= 1 else ''

        super().__init__(root)
        width = 600
        height = 300
        self.title('Painel dos clientes')
        self.geometry(f'{width}x{height}')
        _ = self.columnconfigure(0, weight=1)
        _ = self.rowconfigure(0, weight=1)

        self.protocol('WM_DELETE_WINDOW', self.close)

        self.frm: ttk.Frame = ttk.Frame(self)
        self.frm.grid(sticky='snew')
        self.frm.master.maxsize(width, height)  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
        _ = self.frm.rowconfigure(0, weight=1)
        _ = self.frm.columnconfigure(0, weight=1)
        _ = self.frm.columnconfigure(1, weight=2)

        self.lbl_senha: ttk.Label = ttk.Label(
            self.frm, text='---', font=('TkDefaultFont', 44)
        )
        self.lbl_senha.grid(row=0, column=0)

        self.lbl_hist: ttk.Label = ttk.Label(self.frm, text='Senhas anteriores:')
        self.lbl_hist.grid(row=0, column=1)
        self.update_hist()

    def close(self):
        if self.winfo_ismapped():
            self.withdraw()

    def open(self):
        if not self.winfo_ismapped():
            self.deiconify()

    def toggle(self):
        if self.winfo_ismapped():
            self.withdraw()
        else:
            self.deiconify()

    def reveal(self, senha: str, tipo: str):
        self.hist.append(self.senha_atual)
        self.update_hist()
        self.senha_atual = senha
        _ = self.lbl_senha.configure(text=self.senha_atual)
        match tipo:
            case 'P':
                _ = self.lbl_senha.configure(foreground='red')
            case _:
                _ = self.lbl_senha.configure(foreground='black')

    def update_hist(self):
        _ = self.lbl_hist.configure(
            text='Senhas anteriores:\n' + '\n'.join(list(self.hist))
        )


if __name__ == '__main__':
    root = JanelaPrincipal()
    ## Tema dos elementos
    # Esse requer uma biblioteca externa:
    # sv_ttk.set_theme("light")
    # Esse é embutido no tkinter:
    s = ttk.Style()
    s.theme_use('clam')
    root.mainloop()
