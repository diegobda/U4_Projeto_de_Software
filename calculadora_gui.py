import tkinter as tk
from tkinter import messagebox

def calcular(operacao):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())

        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "*":
            resultado = n1 * n2
        elif operacao == "/":
            if n2 == 0:
                messagebox.showerror("Erro", "Divisão por zero.")
                return
            resultado = n1 / n2

        lbl_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números.")

janela = tk.Tk()
janela.title("Calculadora U4")
janela.geometry("350x250")

tk.Label(janela, text="Primeiro Número").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Segundo Número").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

frame = tk.Frame(janela)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=lambda: calcular("+")).grid(row=0, column=0)
tk.Button(frame, text="-", width=5, command=lambda: calcular("-")).grid(row=0, column=1)
tk.Button(frame, text="*", width=5, command=lambda: calcular("*")).grid(row=0, column=2)
tk.Button(frame, text="/", width=5, command=lambda: calcular("/")).grid(row=0, column=3)

lbl_resultado = tk.Label(janela, text="Resultado:")
lbl_resultado.pack(pady=15)

janela.mainloop()
