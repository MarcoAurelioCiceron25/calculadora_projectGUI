from tkinter import Tk, Entry, Button, StringVar, Label, colorchooser, font

# Inicializa la ventana principal
root = Tk()
root.title("Calculadora")
root.geometry("300x400")

# Variables para el campo de texto
entrada = StringVar()

# Función para actualizar el texto en el campo
def click(boton):
    entrada.set(entrada.get() + str(boton))

# Función para evaluar el resultado
def calcular():
    try:
        resultado = eval(entrada.get())  # Evalúa la expresión matemática
        entrada.set(resultado)
    except:
        entrada.set("Error")

# Función para limpiar el campo de texto
def limpiar():
    entrada.set("")

# Función para cambiar el color de fondo
def cambiar_color():
    color = colorchooser.askcolor(title="Selecciona un color")[1]
    if color:
        root.configure(bg=color)

# Función para cambiar la fuente del campo de texto
def cambiar_fuente():
    fuente_actual = campo_texto["font"]
    nueva_fuente = font.Font(font=fuente_actual).actual()
    nueva_fuente["size"] = 25  # Cambiar tamaño
    nueva_fuente["family"] = "Comic Sans MS"  # Cambiar tipo de fuente
    campo_texto.configure(font=nueva_fuente)

def cambiar_colores_botones():
    color = colorchooser.askcolor(title="Selecciona un color para los botones")[1]
    if color:
        for widget in root.winfo_children():
            if isinstance(widget, Button):
                widget.configure(bg=color)

boton_cambiar_colores = Button(root, text="Cambiar Colores", command=cambiar_colores_botones, font=("Arial", 10))
boton_cambiar_colores.grid(row=6, column=0, columnspan=4)


# Campo de texto
campo_texto = Entry(root, textvariable=entrada, font=("Arial", 20), justify="right")
campo_texto.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Botones de la calculadora
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for texto, fila, columna in botones:
    if texto == "=":
        boton = Button(root, text=texto, command=calcular, font=("Arial", 15), width=5, height=2)
    elif texto == "C":
        boton = Button(root, text=texto, command=limpiar, font=("Arial", 15), width=5, height=2)
    else:
        boton = Button(root, text=texto, command=lambda t=texto: click(t), font=("Arial", 15), width=5, height=2)
    boton.grid(row=fila, column=columna)

# Botones para personalización
boton_color = Button(root, text="Color", command=cambiar_color, font=("Arial", 10), width=10, height=1)
boton_color.grid(row=5, column=0, columnspan=2)

boton_fuente = Button(root, text="Fuente", command=cambiar_fuente, font=("Arial", 10), width=10, height=1)
boton_fuente.grid(row=5, column=2, columnspan=2)

# Ejecuta la ventana
root.mainloop()
