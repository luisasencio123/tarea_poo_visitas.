import tkinter as tk
from tkinter import ttk, messagebox

class AppTkinter:
    def __init__(self, servicio):
        self.servicio = servicio

        self.root = tk.Tk()
        self.root.title("Sistema de Visitantes")
        self.root.geometry("600x400")

        self.crear_widgets()

    def crear_widgets(self):
        # Formulario
        tk.Label(self.root, text="Cédula").pack()
        self.entry_cedula = tk.Entry(self.root)
        self.entry_cedula.pack()

        tk.Label(self.root, text="Nombre").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        tk.Label(self.root, text="Motivo").pack()
        self.entry_motivo = tk.Entry(self.root)
        self.entry_motivo.pack()

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Registrar", command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=2, padx=5)

        # Tabla
        self.tree = ttk.Treeview(self.root, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        if self.servicio.registrar_visitante(cedula, nombre, motivo):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Cédula ya registrada")

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for v in self.servicio.obtener_visitantes():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))

    def eliminar(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        valores = self.tree.item(seleccionado, "values")
        cedula = valores[0]

        if self.servicio.eliminar_visitante(cedula):
            messagebox.showinfo("Éxito", "Visitante eliminado")
            self.actualizar_tabla()

    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def run(self):
        self.root.mainloop()