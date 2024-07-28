import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# Dados de exemplo (preços diários)
data = {
    'Date': pd.date_range(start='2022-12-01', end='2022-12-31'),
    'Price': [100, 110, 105, 115, 120, 125, 130, 128, 135, 140,
              148, 155, 160, 165, 170, 175, 180, 185, 190, 195,   
              260, 258, 265, 270, 275, 280, 285, 290, 288, 295, 234]
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Função para plotar o gráfico
def plot_graph():
    fig = Figure(figsize=(8, 6))
    plot = fig.add_subplot(111)
    plot.plot(df.index, df['Price'], color='blue', marker='o', linestyle='-')
    plot.set_title('Gráfico de Preços')
    plot.set_xlabel('Data')
    plot.set_ylabel('Preço')
    plot.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Criando a interface gráfica com Tkinter
root = tk.Tk()
root.title('Dashboard de Preços')

# Botão para plotar o gráfico
plot_button = tk.Button(root, text="Plotar Gráfico", command=plot_graph)
plot_button.pack(side=tk.BOTTOM)

root.mainloop()
