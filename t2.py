import tkinter as tk
from datetime import datetime, timedelta
import time

class ContadorProgressivo:
    def __init__(self, master, initial_date):
        self.master = master
        self.current_date = datetime.strptime(initial_date, "%Y-%m-%d %H:%M:%S")

        self.label = tk.Label(master, text="Tempo sem contato com a filial de Caponga:", font=("Arial", 24))
        self.label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.contador_label = tk.Label(master, text="", font=("Arial", 42))
        self.contador_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.atualizar_contador()

    def calcular_tempo_decorrido(self):
        while True:
            current_datetime = datetime.now()
            time_difference = current_datetime - self.current_date
            
            days = time_difference.days
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            self.contador_label.config(text=f"{days} dias, {hours}:{minutes}:{seconds}")
            self.master.update()
            time.sleep(1)

    def atualizar_contador(self):
        self.calcular_tempo_decorrido()

# Data inicial
data_inicial = "2024-01-25 22:40:00"

root = tk.Tk()
root.title("Contador de Sumiço do Capongueiro")
root.geometry("800x600")  # Define o tamanho da janela

app = ContadorProgressivo(root, data_inicial)
root.mainloop()
