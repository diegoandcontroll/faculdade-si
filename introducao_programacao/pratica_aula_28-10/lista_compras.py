import tkinter as tk
from tkinter import messagebox
import json
import os

class Item:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def to_dict(self):
        return {"nome": self.nome, "categoria": self.categoria, "preco": self.preco}


class ListaDeCompras:
    def __init__(self, arquivo_json="lista_de_compras.json"):
        self.arquivo_json = arquivo_json
        self.itens = []
        self.carregar_do_arquivo()

    def adicionar_item(self, nome, categoria, preco):
        item = Item(nome, categoria, preco)
        self.itens.append(item)

    def remover_item(self, nome):
        for item in self.itens:
            if item.nome == nome:
                self.itens.remove(item)
                return True
        return False

    def exibir_lista(self):
        if not self.itens:
            return "O carrinho está vazio."
        else:
            lista = "Lista de Compras:\n"
            for item in self.itens:
                lista += f"{item.nome} ({item.categoria}) - R${item.preco:.2f}\n"
            lista += f"\nValor total: R${self.calcular_total():.2f}"
            return lista

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def salvar_em_arquivo(self):
        lista_dict = [item.to_dict() for item in self.itens]
        with open(self.arquivo_json, "w") as file:
            json.dump(lista_dict, file, indent=4)
        print("Lista de compras salva em", self.arquivo_json)

    def carregar_do_arquivo(self):
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r") as file:
                lista_dict = json.load(file)
                self.itens = [Item(**item) for item in lista_dict]


class InterfaceListaDeCompras:
    def __init__(self, root):
        self.lista_de_compras = ListaDeCompras()

        # Configuração da janela principal
        self.root = root
        self.root.title("Lista de Compras Inteligente")
        self.root.geometry("400x400")  # Define um tamanho fixo

        # Centraliza a janela principal
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Frame principal centralizado
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        # Widgets dentro do frame
        self.label_nome = tk.Label(self.frame, text="Nome do Item:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_categoria = tk.Label(self.frame, text="Categoria:")
        self.label_categoria.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_categoria = tk.Entry(self.frame)
        self.entry_categoria.grid(row=1, column=1, padx=5, pady=5)

        self.label_preco = tk.Label(self.frame, text="Preço (R$):")
        self.label_preco.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_preco = tk.Entry(self.frame)
        self.entry_preco.grid(row=2, column=1, padx=5, pady=5)

        # Botões
        self.button_adicionar = tk.Button(self.frame, text="Adicionar Item", command=self.adicionar_item)
        self.button_adicionar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.button_remover = tk.Button(self.frame, text="Remover Item", command=self.remover_item)
        self.button_remover.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.button_exibir = tk.Button(self.frame, text="Exibir Lista", command=self.exibir_lista)
        self.button_exibir.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.button_sair = tk.Button(self.frame, text="Sair", command=self.sair)
        self.button_sair.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def adicionar_item(self):
        nome = self.entry_nome.get()
        categoria = self.entry_categoria.get()
        try:
            preco = float(self.entry_preco.get())
            if nome and categoria:
                self.lista_de_compras.adicionar_item(nome, categoria, preco)
                messagebox.showinfo("Sucesso", f"Item '{nome}' adicionado ao carrinho.")
                self.entry_nome.delete(0, tk.END)
                self.entry_categoria.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
            else:
                messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um preço válido.")

    def remover_item(self):
        nome = self.entry_nome.get()
        if nome:
            if self.lista_de_compras.remover_item(nome):
                messagebox.showinfo("Sucesso", f"Item '{nome}' removido do carrinho.")
            else:
                messagebox.showwarning("Aviso", f"Item '{nome}' não encontrado no carrinho.")
            self.entry_nome.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do item para remover.")

    def exibir_lista(self):
        lista = self.lista_de_compras.exibir_lista()
        messagebox.showinfo("Lista de Compras", lista)

    def sair(self):
        # Salva a lista de compras em um arquivo JSON antes de sair
        self.lista_de_compras.salvar_em_arquivo()
        messagebox.showinfo("Sair", "Lista de compras salva em 'lista_de_compras.json'.")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceListaDeCompras(root)
    root.mainloop()
