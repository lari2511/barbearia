import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Valores fixos dos serviços
servicos = [
    ("Corte", 45.00),
    ("Corte Kids", 50.00),
    ("Corte Máquina 1", 35.00),
    ("Corte Raspado Navalha", 35.00),
    ("Sombrancelha", 20.00),
    ("Pezinho", 20.00),
    ("Pezinho Navalha", 25.00),
    ("Abaixar Barba Máquina", 15.00),
    ("Limpar Pescoço / Bigode", 25.00),
    ("Combo Corte e Barba", 70.00),
    ("Combo Corte Máquina e Barba", 60.00),
    ("Combo Raspado e Barba", 60.00),
    ("Barba", 40.00),
]

# Função de cálculo
def calcular():
    try:
        total_allan = 0
        total_marcos = 0

        for i, (_, valor) in enumerate(servicos):
            qtd_allan = int(allan_entries[i].get() or 0)
            qtd_marcos = int(marcos_entries[i].get() or 0)

            total_allan += qtd_allan * valor
            total_marcos += qtd_marcos * valor

        total_allan /= 2  # Allan divide com Marcos
        total_allan_label.config(text=f"Total Allan (50%): R$ {total_allan:.2f}")
        total_marcos_label.config(text=f"Total Marcos (100%): R$ {total_marcos:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos com números inteiros.")

# Janela principal
root = tk.Tk()
root.title("Barbearia O Patriarca")
root.geometry("1000x720")

# Fundo com imagem (opcional)
try:
    bg = Image.open("logo_patriarca.jpeg").resize((1000, 720))
    bg = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(root, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Imagem de fundo não carregada:", e)

# Título
tk.Label(root, text="Serviços da Barbearia O Patriarca", font=("Arial", 16, "bold")).place(x=300, y=10)

# Cabeçalho
tk.Label(root, text="Serviço", font=("Arial", 12, "bold")).place(x=50, y=50)
tk.Label(root, text="Allan", font=("Arial", 12, "bold")).place(x=400, y=50)
tk.Label(root, text="Marcos", font=("Arial", 12, "bold")).place(x=550, y=50)

# Listas para armazenar os campos
allan_entries = []
marcos_entries = []

# Gerar os campos para cada serviço
for idx, (nome_servico, valor) in enumerate(servicos):
    y = 80 + idx * 35

    tk.Label(root, text=f"{nome_servico} (R$ {valor:.2f})", font=("Arial", 10), anchor="w", width=30).place(x=50, y=y)

    entry_allan = tk.Entry(root, width=5)
    entry_allan.place(x=400, y=y)
    allan_entries.append(entry_allan)

    entry_marcos = tk.Entry(root, width=5)
    entry_marcos.place(x=550, y=y)
    marcos_entries.append(entry_marcos)

# Botão calcular
tk.Button(root, text="Calcular", command=calcular, width=20, bg="green", fg="white").place(x=400, y=550)

# Labels de resultado
total_allan_label = tk.Label(root, text="Total Allan (50%): R$ 0.00", font=("Arial", 12))
total_allan_label.place(x=100, y=600)

total_marcos_label = tk.Label(root, text="Total Marcos (100%): R$ 0.00", font=("Arial", 12))
total_marcos_label.place(x=500, y=600)

root.mainloop()
