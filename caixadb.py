import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
import sqlite3

conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL,
    internal_code INTEGER NOT NULL,
    code TEXT UNIQUE
)
''')
conn.commit()

consulta = tk.Tk()
consulta.title("Consulta")
consulta.config(width=150, height=100)
addProd = tk.Toplevel(consulta)
addProd.title("Adicionar Produto")
addProd.withdraw()
addProd.config(width=150, height=100)
productList = tk.Toplevel(consulta)
productList.title("Produtos")
productList.withdraw()
productList.config(width=150, height=100)

menu_bar = Menu(consulta)

def seeConsulta():
    consulta.deiconify()
    addProd.withdraw()
    productList.withdraw()
    return
def seeAddProd():
    consulta.withdraw()
    addProd.deiconify()
    productList.withdraw()
    return
def seeProductList():
    consulta.withdraw()
    addProd.withdraw()
    productList.deiconify()
    return
def addProduct():
    try:
        price = float(priceEntry.get())
        estoque = int(stockEntry.get())
        internalCode = int(codigoInternoEntry.get())
        
        cursor.execute("INSERT INTO produtos (product_name, price, stock, internal_code, code) VALUES (?, ?, ?, ?, ?)",
                       (name_product_entry.get(), price, estoque, internalCode, codProduct.get()))
        
        conn.commit()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar produto: {e}")
def consultar():
    try:
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        
        for prod in produtos:
            internal_code = prod[4] 
            
            if internal_code == int(codigoProd.get()):
                print(prod)
                product_name_label.config(text=prod[1])
                codigoInt.config(text=prod[5])
                preco.config(text=prod[2])
                estoque.config(text=prod[3])
                return
        
        print("Produto não encontrado.")
    
    except Exception as e:
        print(f"Erro ao consultar: {e}")

menu_arquivo = Menu(menu_bar, tearoff = 0)
menu_options = Menu(menu_bar, tearoff = 0)
menu_arquivo.add_command(label="Sair", command=consulta.quit)
menu_options.add_command(label="Consulta", command=seeConsulta)
menu_options.add_command(label="Add Produto", command=seeAddProd)
menu_options.add_command(label="Lista Produtos", command=seeProductList)

menu_bar.add_cascade(label="File", menu=menu_arquivo)
menu_bar.add_cascade(label="Options", menu=menu_options)

consulta.config(menu=menu_bar)
addProd.config(menu=menu_bar)
productList.config(menu=menu_bar)

#Interações
##Consultar
codigoProdLabel = tk.Label(consulta, text="Codigo do produto")
codigoProd = tk.Entry(consulta)
product_name_label_2 = tk.Label(consulta, text="Product Name")
product_name_label= tk.Label(consulta, text="")
codigoIntLabel = tk.Label(consulta, text="Codigo Interno")
codigoInt = tk.Label(consulta, text="")
preco_label= tk.Label(consulta, text="Preço")
preco = tk.Label(consulta, text="")
estoque_label2= tk.Label(consulta, text="Estoque")
estoque = tk.Label(consulta,text="")
consulta_btn = tk.Button(consulta, text="Consultar", command=consultar)
##Adicionar Produto
name_product_label = tk.Label(addProd, text="Nome Produto")
name_product_entry = tk.Entry(addProd)
codigoProdLabel2 = tk.Label(addProd, text="Codigo do produto")
codProduct = tk.Entry(addProd)
codigoInterno =  tk.Label(addProd, text="Codigo Interno")
codigoInternoEntry = tk.Entry(addProd)
priceLabel = tk.Label(addProd,text="Price")
priceEntry = tk.Entry(addProd)
stockLabel = tk.Label(addProd, text="Estoque")
stockEntry = tk.Entry(addProd)
add_btn = tk.Button(addProd, text="Adicionar", command=addProduct)

#pack
##Consulta
codigoProdLabel.pack()
codigoProd.pack()
product_name_label_2.pack()
product_name_label.pack()
codigoIntLabel.pack()
codigoInt.pack()
preco_label.pack()
preco.pack()
estoque_label2.pack()
estoque.pack()
consulta_btn.pack()
##AddProduct
name_product_label.pack()
name_product_entry.pack()
codigoProdLabel2.pack()
codProduct.pack()
codigoInterno.pack()
codigoInternoEntry.pack()
priceLabel.pack()
priceEntry.pack()
stockLabel.pack()
stockEntry.pack()
add_btn.pack()

try:
    consulta.mainloop()
except KeyboardInterrupt:
    print("Programa Encerrado")