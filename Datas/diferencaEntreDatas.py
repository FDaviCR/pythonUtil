from datetime import datetime

data_atual = datetime.now()
data_final = datetime(2025, 2, 20, 8, 30, 0)

diferenca = data_final - data_atual

print(f"Diferença em dias: {diferenca.days}")
print(f"Diferença em minutos: {diferenca.total_seconds()/60}")
print(f"Diferença em horas: {(diferenca.total_seconds()/60)/60}")
print(f"Diferença total em segundos: {diferenca.total_seconds()}")


