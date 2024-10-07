import tkinter as tk
from tkinter import ttk
import tela1

class Tela2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Tela 2", font=("Helvetica", 24))
        label.pack(pady=20, padx=20)

        # Botão para voltar para a Tela 1
        botao_ir_tela1 = ttk.Button(self, text="Voltar para a Tela 1",
                                    command=lambda: controller.mostrar_tela(tela1.Tela1))
        botao_ir_tela1.pack(pady=10)
