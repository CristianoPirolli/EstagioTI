import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def contar_caracteres_coluna_a(caminho_arquivo_csv):
    codificacoes = ['utf-8', 'utf-16', 'latin1']
    for cod in codificacoes:
        try:
            with open(caminho_arquivo_csv, mode='r', encoding=cod) as arquivo:
                leitor = csv.reader(arquivo)
                resultados = []
                for i, linha in enumerate(leitor, start=1):
                    if len(linha) >= 1:
                        qtd_caracteres = len(linha[0])
                        resultados.append(f"Linha {i}: {qtd_caracteres} caracteres")
                    else:
                        resultados.append(f"Linha {i}: 0 caracteres (coluna A vazia)")
                return resultados
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("Erro de codificação", b"", 0, 1, "Nenhuma codificação funcionou")



def selecionar_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not caminho:
        return

    try:
        resultado = contar_caracteres_coluna_a(caminho)
        mostrar_resultado(resultado)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível processar o arquivo:\n{e}")

def mostrar_resultado(linhas):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultado")
    texto = tk.Text(janela_resultado, wrap="word", width=80, height=20)
    texto.pack(padx=10, pady=10)
    texto.insert("1.0", "\n".join(linhas))
    texto.config(state="disabled")

# Janela principal
janela = tk.Tk()
janela.title("Contador de Caracteres - Coluna A (CSV)")

label = tk.Label(janela, text="Clique no botão para selecionar um arquivo CSV:")
label.pack(pady=10)

botao = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo)
botao.pack(pady=5)

janela.mainloop()
