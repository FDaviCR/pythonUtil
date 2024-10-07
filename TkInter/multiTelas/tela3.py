import tkinter as tk
from tkinter import ttk
from tela2 import Tela2

class Tela3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Tela 3", font=("Helvetica", 24))
        label.pack(pady=20, padx=20)

        # Botão para ir para a Tela 2
        botao_ir_tela2 = ttk.Button(self, text="Ir para a Tela 2",
                                    command=lambda: controller.mostrar_tela(Tela2))
        botao_ir_tela2.pack(pady=10)
