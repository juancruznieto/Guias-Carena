import tkinter as tk
from tkinter import StringVar, ttk
from ttkbootstrap import Style
from centrar_ventana import centrar

#Tamaño del formulario, ancho=360, alto=249, puede usar centrar_ventana.
root = tk.Tk()
root.geometry('360x249')
root.title('IE2 - Programación II')

#En la línea siguiente al crear el formulario o la ventana, aplicar el estilo con:
Style = Style("darkly")

#Insertar un frame (marco) con el nombre frame y el siguiente código:
frame = ttk.Frame(root, padding='10 10 10 10', height=240, width=300, borderwidth=2, relief='sunken')
frame.pack()

#Cada widget debe estar en una grilla dentro del frame con un padx=5 y un pady=5.
#Insertar tres label con el nombre label1, label2, y label3 como muestra la imágen, con su respectivo text y width=15.
label1 = tk.Label(frame, width=15, text='Valor 1:')
label1.grid(padx=5, pady=5)

label2 = tk.Label(frame, width=15, text='Valor 2:')
label2.grid(padx=5, pady=5)

label3 = tk.Label(frame, width=15, text='Resultado:')
label3.grid(padx=5, pady=5)


#Insertar tres entry con el nombre entry1, entry2, entry3 y con width=15, validate=’key’ para el primero y segundo y el último entry debe tener la propiedad state=”disabled” para no permitir el ingreso de datos.
entry1 = tk.Entry(frame, validate = "key", width=15)
entry1.grid(column=4, row=0, padx=10, pady=10)

entry2 = tk.Entry(frame, validate = "key", width=15)
entry2.grid(column=4, row=1, padx=10, pady=10)

entry3 = tk.Entry(frame, validate = "key", state="disabled" , width=15)
entry3.grid(column=4, row=2, padx=10, pady=10)

#Los dos primeros entry deben permitir solo el ingreso de valores enteros sin punto decimal ni negativos, solo dígitos, con una longitud de hasta 7 caracteres.
def validate_entry(action, previous_text, new_text, text):
    print('1 Acción', action)
    print('2 Texto previo', previous_text)
    print('3 Texto que se está ingresando', new_text)
    print('4 Texto si el resultado es True', text,' \n')

    if not new_text.isdigit() and new_text != '.':
        return False

    if len(previous_text) == 10 and action != '0':
        return False

    if action == '0':
        return True

    if new_text == '.' and previous_text.find('.') != -1:
        return False

    punto = previous_text.find('.')

    if new_text.isdigit():

        if punto == -1:
            if len(previous_text) == 7:
                return False
        else:
            if len(previous_text[:punto - 1]) == 7:
                return False

    if punto != -1 and len(previous_text[punto + 1:]) == 2:
        return False

    return True

entry1['validatecommand'] = (entry1.register(validate_entry), '%d',  '%s', '%S', '%P')
entry2['validatecommand'] = (entry2.register(validate_entry), '%d',  '%s', '%S', '%P')

#Definir una función limpiar que responda al botón con el mismo nombre referenciando la función con la propiedad command=limpiar desde el entry3:
def limpiar():
    entry1.delete(0, tk.END)

    entry2.delete(0, tk.END)

    entry3.config(state='normal')
    entry3.delete(0, tk.END)
    entry3.config(state='disabled')

    entry1.focus()

    return

#Para el entry3 que nos guarda el resultado es muy conveniente utilizar la clase StringVar para asociar una variable a un entry, seguir como muestra el ejemplo (ver video de StringVar):

resultado = StringVar()
entry3 = tk.Entry(frame, width=15, state='disabled', textvariable=resultado, validatecommand=limpiar)
entry3['validatecommand'] = (entry3.register(limpiar), '%d', '%s', '%S', '%i')

#Insertar seis botones en tres filas, dos en cada una con las consignas de la definición de sus respectivas funciones serán entregadas y realizadas en el instituto en el horario y fecha de la IE2.
button1 = tk.Button(frame, text='+', width=15)
button1.grid(column=0, row=3, padx=5, pady=5)

button2 = tk.Button(frame, text='-', width=15)
button2.grid(column=4, row=3, padx=5, pady=5)

button3 = tk.Button(frame, text='*', width=15)
button3.grid(column=0, row=4, padx=5, pady=5)

button4 = tk.Button(frame, text='/', width=15)
button4.grid(column=4, row=4, padx=5, pady=5)

button5 = tk.Button(frame, text='%', width=15)
button5.grid(column=0, row=5, padx=5, pady=5)

button6 = tk.Button(frame, text='LIMPIAR', width=15)
button6.grid(column=4, row=5, padx=5, pady=5)





















root.mainloop()