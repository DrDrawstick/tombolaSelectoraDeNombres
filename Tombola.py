import tkinter as tk
import random
from tkinter import messagebox

class NombreMascotaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Selector de Nombres para Mascota")
        self.nombres = []

        # Cuadro de texto para ingresar nombres
        self.nombre_entry = tk.Entry(root, width=30)
        self.nombre_entry.grid(row=0, column=0, padx=10, pady=10)

        # Botón para agregar nombres
        self.agregar_boton = tk.Button(root, text="Agregar Nombre", command=self.agregar_nombre)
        self.agregar_boton.grid(row=0, column=1, padx=10, pady=10)

        # Listbox para mostrar los nombres agregados
        self.nombres_listbox = tk.Listbox(root, width=50, height=10)
        self.nombres_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para eliminar nombres
        self.eliminar_boton = tk.Button(root, text="Este no :c", command=self.eliminar_nombre)
        self.eliminar_boton.grid(row=2, column=0, padx=10, pady=10)

        # Botón para girar la tómbola
        self.girar_boton = tk.Button(root, text="Girar Tómbola", command=self.girar_tombola)
        self.girar_boton.grid(row=2, column=1, padx=10, pady=10)

        # Label para mostrar el nombre seleccionado
        self.resultado_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def agregar_nombre(self):
        nombre = self.nombre_entry.get()
        if nombre:
            self.nombres.append(nombre)
            self.nombres_listbox.insert(tk.END, nombre)
            self.nombre_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")

    def eliminar_nombre(self):
        selected_index = self.nombres_listbox.curselection()
        if selected_index:
            nombre = self.nombres_listbox.get(selected_index)
            self.nombres.remove(nombre)
            self.nombres_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un nombre para eliminar.")

    def girar_tombola(self):
        if len(self.nombres) < 3:
            messagebox.showwarning("Advertencia", "Mínimo agregue 3 nombres para que la tómbola tenga sentido.")
        else:
            nombre_aleatorio = random.choice(self.nombres)
            self.resultado_label.config(text=f"Nombre seleccionado: {nombre_aleatorio}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NombreMascotaApp(root)
    root.mainloop()
