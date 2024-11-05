import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
MORSES = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

root = tk.Tk()
root.title("Morse")

root2 = tk.Toplevel(root)
root2.title("Translator")
root2.withdraw()
cod = []
resu = []

menu_bar = Menu(root)

def clear():
    resu = []
    cod = []
    result.config(text="")
    result2.config(text="")
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)

def mostrarJanela1():
    root2.withdraw()
    root.deiconify()
    return
def mostrarJanela2():
    root.withdraw()
    root2.deiconify()
    return

def janela2():
    return

##Code Root1()

def morse():
    palavra = entry.get()
    cod = []
    for letra in palavra:
        if letra.upper() in LETTERS:
            posicao = LETTERS.index(letra.upper())
            cod.append(MORSES[posicao])
            
    result.config(text=cod)
    return ' '.join(cod)

def copy():
    root.clipboard_clear()
    text_to_copy = result.cget("text")
    root.clipboard_append(text_to_copy)
    messagebox.showinfo("Copiado!", f"The Copied Text is {text_to_copy}")
    return

##Code Root2()
def translate():
    palavra = entry2.get()
    resu = []

    for letra in palavra.split():
        if letra == "/":
            resu.append(" ")
        elif letra in MORSES:
            posicao = MORSES.index(letra)
            resu.append(LETTERS[posicao])
        else:
            resu.append("?")
    result2.config(text=''.join(resu))
    return

def copy2():
    root2.clipboard_clear()
    text_to_copy = result2.cget("text")
    root2.clipboard_append(text_to_copy)
    messagebox.showinfo("Copy!", f"The Copied Text is {text_to_copy}")
    return

menu_arquivo = Menu(menu_bar, tearoff=0)
menu_options = Menu(menu_bar, tearoff=0)
menu_options.add_command(label="Morse", command=mostrarJanela1)
menu_options.add_command(label="Translator", command=mostrarJanela2)
menu_arquivo.add_command(label="Clear", command=clear)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)

menu_bar.add_cascade(label="File", menu=menu_arquivo)
menu_bar.add_cascade(label="Options", menu=menu_options)

root.config(menu=menu_bar)
root2.config(menu=menu_bar)

#Root1
digite = tk.Label(root,text="Write A Word")
entry = tk.Entry(root, width=30)
gen = tk.Button(root,text="Gerar", command=morse)
resultado = tk.Label(root,text="Result")
result = tk.Label(root,text="")
copiar = tk.Button(root,text="Copy", command=copy)
#Root2
digite2 = tk.Label(root2,text="Write Code")
entry2 = tk.Entry(root2, width=30)
translatebtn = tk.Button(root2, text="Translate", command=translate)
resultado2 = tk.Label(root2, text="Result")
result2 = tk.Label(root2, text="")
copiar2 = tk.Button(root2, text="Copy!", command=copy2)
#Pack()
digite.pack()
entry.pack()
gen.pack()
resultado.pack()
result.pack()
copiar.pack()

#Pack2()
digite2.pack()
entry2.pack()
translatebtn.pack()
resultado2.pack()
result2.pack()
copiar2.pack()
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Programa Encerrado")