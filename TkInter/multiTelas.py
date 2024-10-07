import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicativo Multi-Telas")
        self.geometry("400x300")
        
        # Container que irá segurar todas as telas (frames)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        # Configuração para expandir adequadamente
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (Tela1, Tela2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.mostrar_tela(Tela1)
    
    def mostrar_tela(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Tela1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Tela 1", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)
        
        botao_ir_tela2 = ttk.Button(self, text="Ir para a Tela 2",
                                    command=lambda: controller.mostrar_tela(Tela2))
        botao_ir_tela2.pack()

class Tela2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Tela 2", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)
        
        botao_ir_tela1 = ttk.Button(self, text="Voltar para a Tela 1",
                                    command=lambda: controller.mostrar_tela(Tela1))
        botao_ir_tela1.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
