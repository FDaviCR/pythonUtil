from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from datetime import datetime

data_atual = datetime.now()
data_final = datetime(2025, 2, 20, 8, 30, 0)

diferenca = data_final - data_atual

class CountdownApp(App):
    
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.dias = Label(text=f"{diferenca.days}")
        layout.add_widget(self.dias)
        
        self.semanas = Label(text=f"{diferenca.days/7}")
        layout.add_widget(self.semanas)

        Window.size = (300, 600)
        return layout

if __name__ == "__main__":
    CountdownApp().run()
