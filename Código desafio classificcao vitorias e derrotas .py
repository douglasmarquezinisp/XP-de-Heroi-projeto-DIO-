import tkinter as tk
from tkinter import simpledialog, messagebox

# Parti para criação de caixas tipo windowns para entrada e saida do resultado
root = tk.Tk()
root.withdraw()

# Montando as 03 caixas onde faz entrada do nome, vitorias e derrotas
nome = simpledialog.askstring("Input", "Digite o nome do herói:", parent=root)
vitorias = simpledialog.askinteger("Input", "Digite a quantidade de vitórias do herói:", parent=root, minvalue=0, maxvalue=150000)
derrotas = simpledialog.askinteger("Input", "Digite a quantidade de derrotas do herói:", parent=root, minvalue=0, maxvalue=150000)

# calcular a base para obter resulto
saldo_vitorias = vitorias - derrotas

# Classificação de acordo com o Desafio DIO
if saldo_vitorias < 10:
    nivel = "Ferro"
elif 11 <= saldo_vitorias <= 20:
    nivel = "Bronze"
elif 21 <= saldo_vitorias <= 50:
    nivel = "Prata"
elif 51 <= saldo_vitorias <= 80:
    nivel = "Ouro"
elif 81 <= saldo_vitorias <= 90:
    nivel = "Diamante"
elif 91 <= saldo_vitorias <= 100:
    nivel = "Lendário"
else: # Saldo de vitórias é maior ou igual a 101
    nivel = "Imortal"

# Aqui informar também o resultado em uma janela tipo windowns
messagebox.showinfo("Resultado", f"O Herói {nome} com saldo de vitórias {saldo_vitorias} está no nível {nivel}")
