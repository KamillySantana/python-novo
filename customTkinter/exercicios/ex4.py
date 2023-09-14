import customtkinter as tk

tk.set_appearance_mode('ligth')
janela = tk.CTk()
janela.title('Exercicio')
janela.geometry('500x400')
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

informe = tk.CTkLabel(janela, text='Calculadora', font=('Arial',20))
informe.grid(row=1, column=6)

num = tk.CTkEntry(janela, placeholder_text='Digite um numero',width=200, height=30)
num.grid(row=2, column=6)
texto = num.get()

num2 = tk.CTkEntry(janela, placeholder_text='Digite um segundo numero',width=200, height=30)
num2.grid(row=3, column=6)
texto2 = num2.get()

# Operadores
operadores = tk.CTkLabel(janela, text='Digite +, -, *, / ou **(elevado) para calcular', font=('Arial',15))
operadores.grid(row=4, column=6)

infOperadores = tk.CTkEntry(janela, placeholder_text='Digite operador',width=200, height=30)
infOperadores.grid(row=5, column=6)
texto3 = infOperadores.get()

def calcular():
    n1 = float(num.get())
    n2 = float(num2.get())

    operadorCon = str(infOperadores.get())

    if operadorCon == "+":
        resultado = n1 + n2
    elif operadorCon == "-":
        resultado = n1 - n2
    elif operadorCon == "*":
        resultado = n1 * n2
    elif operadorCon == "/":
        resultado = n1 / n2
    elif operadorCon == "**":
        resultado = n1 ** n2
    else:
        resultado = "Operador inválido"

    exibir.configure(text=resultado)


exibir = tk.CTkLabel(janela, text='')
exibir.grid(row=7, column=6)

botao = tk.CTkButton(janela, text="Calcular", command=calcular)
botao.grid(row=6, column=6)

janela.mainloop()

