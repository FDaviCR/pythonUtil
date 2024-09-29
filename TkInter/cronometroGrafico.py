import tkinter as tk
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(root, text="Iniciar", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(root, text="Parar", command=self.stop)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(root, text="Zerar", command=self.reset)
        self.reset_button.pack(side="left")

    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            hours, remainder = divmod(self.elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.label.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
            self.root.after(1000, self.update)  # Atualiza a cada segundo

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time  # Retoma de onde parou
            self.running = True
            self.update()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.elapsed_time = 0
        self.label.config(text="00:00:00")
        if not self.running:
            self.start_time = time.time()

root = tk.Tk()
cronometro = Cronometro(root)
root.mainloop()
