import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import conexion

class Estudiante:
    def __init__(self):
        self.acciones = conexion.Registro()
        self.ventana = tk.Tk()
        self.ventana.title('Sistema de Estudiantes | Universidad Nacional')
        self.ventana.geometry('635x410')
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap('logo_uma.ico')
        self.cuaderno = ttk.Notebook(self.ventana)
        self.ventana.config(
            bg='gray75'
        )
        self.barra1 = tk.Label(self.ventana)
        self.barra1.config(
            bg='black',
            padx=630,
            pady=20
        )
        self.barra1.grid(row=0)
        self.barra2 = tk.Label(self.ventana)
        self.barra2.config(
            bg='dark olive green',
            padx=630,
            pady=10
        )
        self.barra2.grid(row=0)
        self.texto1 = tk.Label(self.ventana, text='Bienvenido!! Sistema de Registro Estudiantil!!')
        self.texto1.config(
            font=('Arial', 15, 'bold'),
            fg='black',
            bg='gray75'
        )
        self.texto1.grid(row=1,column=0, sticky='nw', pady=5)
        self.cargar()
        self.consultar()
        self.listado()
        self.eliminar()
        self.cuaderno.grid(row=3, column=0, sticky='nw', padx=80, pady=20)
        self.footer = tk.Label(self.ventana, text='Universidad Nacional | Derechos Reservados')
        self.footer.config(
            bg='black',
            fg='white',
            padx=220,
            
        )
        self.footer.grid(row=15, sticky='sw')
        self.ventana.mainloop()

        #Pestañas
    def cargar(self):    
        self.pestaña1 = ttk.Frame(self.cuaderno)
        #campo1
        self.cuaderno.add(self.pestaña1, text='Registrar')
        self.nombre = ttk.Label(self.pestaña1, text='Nombre: ')
        self.nombre.grid(row=4, column=0,  padx=5, pady=5)
        self.carganombre = tk.StringVar()
        self.campo_nombre = tk.Entry(self.pestaña1, textvariable=self.carganombre)
        self.campo_nombre.grid(row=4, column=1)
        #campo2
        self.apellido = ttk.Label(self.pestaña1, text='Apellido: ')
        self.apellido.grid(row=5, column=0,  padx=5, pady=5)
        self.cargaapellido = tk.StringVar()
        self.campo_apellido = tk.Entry(self.pestaña1, textvariable=self.cargaapellido)
        self.campo_apellido.grid(row=5, column=1)
        #campo3
        self.dni = ttk.Label(self.pestaña1, text='DNI: ')
        self.dni.grid(row=6, column=0,  padx=5, pady=5)
        self.cargadni = tk.StringVar()
        self.campo_dni = tk.Entry(self.pestaña1, textvariable=self.cargadni)
        self.campo_dni.grid(row=6, column=1)
        #campo4
        self.telefono = ttk.Label(self.pestaña1, text='Teléfono: ')
        self.telefono.grid(row=4, column=2,  padx=5, pady=5)
        self.cargatelefono = tk.StringVar()
        self.campo_telefono = tk.Entry(self.pestaña1, textvariable=self.cargatelefono)
        self.campo_telefono.grid(row=4, column=3)
        #campo5
        self.email = ttk.Label(self.pestaña1, text='Email: ')
        self.email.grid(row=5, column=2,  padx=5, pady=5)
        self.cargaemail = tk.StringVar()
        self.campo_email = tk.Entry(self.pestaña1, textvariable=self.cargaemail)
        self.campo_email.grid(row=5, column=3)
        #campo6
        self.facultad = ttk.Label(self.pestaña1, text='Facultad: ')
        self.facultad.grid(row=6, column=2,  padx=5, pady=5)
        self.cargafacultad = tk.StringVar()
        self.campo_facultad = tk.Entry(self.pestaña1, textvariable=self.cargafacultad)
        self.campo_facultad.grid(row=6, column=3)
        #campo7
        self.observaciones = ttk.Label(self.pestaña1, text='Observaciones: ')
        self.observaciones.grid(row=7, column=2,  padx=5, pady=5)
        self.cargaobservaciones = tk.StringVar()
        self.campo_observaciones = tk.Entry(self.pestaña1, textvariable=self.cargaobservaciones)
        self.campo_observaciones.grid(row=7, column=3)
        #campo8
        self.boton1 = ttk.Button(self.pestaña1, text="Confirmar",command=self.agregar)
        self.boton1.grid(column=1, row=10, padx=4, pady=4)
        self.boton2 = ttk.Button(self.pestaña1, text="Salir",command=self.ventana.quit)
        self.boton2.grid(column=3, row=10, padx=4, pady=4)

    def agregar(self):
        datos = (self.carganombre.get(), self.cargaapellido.get(), self.cargadni.get(), self.cargatelefono.get(), self.cargaemail.get(), self.cargafacultad.get(), self.cargaobservaciones.get())
        self.acciones.alta(datos)
        mb.showinfo('Información', 'Datos cargados')
        self.carganombre.set('')
        self.cargaapellido.set('')
        self.cargadni.set('')
        self.cargatelefono.set('')
        self.cargaemail.set('')
        self.cargafacultad.set('')
        self.cargaobservaciones.set('')

    def consultar(self):
        self.pestaña2 = ttk.Frame(self.cuaderno)
         #campo1
        self.dni = ttk.Label(self.pestaña2, text='DNI: ')
        self.dni.grid(row=4, column=0,  padx=5, pady=5)
        self.consultadni = tk.StringVar()
        self.campo_dni = tk.Entry(self.pestaña2, textvariable=self.consultadni)
        self.campo_dni.grid(row=4, column=1)
        #campo2
        self.cuaderno.add(self.pestaña2, text='Consultar')
        self.nombre = ttk.Label(self.pestaña2, text='Nombre: ')
        self.nombre.grid(row=6, column=0,  padx=5, pady=5)
        self.consultanombre = tk.StringVar()
        self.campo_nombre = tk.Entry(self.pestaña2, textvariable=self.consultanombre, state="readonly")
        self.campo_nombre.grid(row=6, column=1)
        #campo3
        self.apellido = ttk.Label(self.pestaña2, text='Apellido: ')
        self.apellido.grid(row=7, column=0,  padx=5, pady=5)
        self.consultaapellido = tk.StringVar()
        self.campo_apellido = tk.Entry(self.pestaña2, textvariable=self.consultaapellido, state="readonly")
        self.campo_apellido.grid(row=7, column=1)
        #campo4
        self.telefono = ttk.Label(self.pestaña2, text='Teléfono: ')
        self.telefono.grid(row=8, column=0,  padx=5, pady=5)
        self.consultatelefono = tk.StringVar()
        self.campo_telefono = tk.Entry(self.pestaña2, textvariable=self.consultatelefono, state="readonly")
        self.campo_telefono.grid(row=8, column=1)
        #campo5
        self.email = ttk.Label(self.pestaña2, text='Email: ')
        self.email.grid(row=8, column=0,  padx=5, pady=5)
        self.consultaemail = tk.StringVar()
        self.campo_email = tk.Entry(self.pestaña2, textvariable=self.consultaemail, state="readonly")
        self.campo_email.grid(row=8, column=1)
        #campo6
        self.facultad = ttk.Label(self.pestaña2, text='Facultad: ')
        self.facultad.grid(row=9, column=0,  padx=5, pady=5)
        self.consultafacultad = tk.StringVar()
        self.campo_facultad = tk.Entry(self.pestaña2, textvariable=self.consultafacultad, state="readonly")
        self.campo_facultad.grid(row=9, column=1)
        #campo7
        self.observaciones = ttk.Label(self.pestaña2, text='Observaciones: ')
        self.observaciones.grid(row=10, column=0,  padx=5, pady=5)
        self.consultaobservaciones = tk.StringVar()
        self.campo_observaciones = tk.Entry(self.pestaña2, textvariable=self.consultaobservaciones, state="readonly")
        self.campo_observaciones.grid(row=10, column=1)
        #campo8
        self.boton1 = ttk.Button(self.pestaña2, text="Consultar",command=self.buscar)
        self.boton1.grid(column=0, row=11, padx=4, pady=4)
        self.boton2 = ttk.Button(self.pestaña2, text="Salir", command=self.ventana.quit)
        self.boton2.grid(column=1, row=11, padx=4, pady=4)

    def buscar(self):
        datos = (self.consultadni.get(), )
        respuesta = self.acciones.consulta(datos)
        if len(respuesta)>0:
            self.consultanombre.set(respuesta[0][1])
            self.consultaapellido.set(respuesta[0][2])
            self.consultatelefono.set(respuesta[0][4])
            self.consultaemail.set(respuesta[0][5])
            self.consultafacultad.set(respuesta[0][6])
            self.consultaobservaciones.set(respuesta[0][7])
        else:
            self.consultadni.set('')
            mb.showinfo("Información", "No existe el estudiante.Intenta de nuevo")

    def listado(self):
        self.pestaña3 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pestaña3, text="Listado")
        self.labelframe3=ttk.LabelFrame(self.pestaña3)
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado Estudiante (completo)",command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=50, height=8)
        self.scrolledtext1.config(
            bg="gray59",
        )
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)      

    def listar(self):
        respuesta=self.acciones.todo()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "ID:"+str(fila[0])+"\nNombre:"+fila[1]+"\nApellido:"+fila[2]+"\nDNI:"+str(fila[3])+"\nTeléfono:"+str(fila[4])+"\nEmail:"+fila[5]+"\nFacultad:"+fila[6]+"\nObservaciones:"+fila[7]+"\n\n")

    def eliminar(self):
        self.pestaña4 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pestaña4, text="Eliminar")
        self.el_dni = ttk.Label(self.pestaña4,text="DNI: ")
        self.el_dni.grid(row=3, column=0,  padx=5, pady=10)
        self.carga_dni = tk.StringVar()
        self.campo_el_dni = ttk.Entry(self.pestaña4, textvariable=self.carga_dni)
        self.campo_el_dni.grid(row=3, column=1)
        self.boton1=ttk.Button(self.pestaña4, text="Eliminar",command=self.borrar)
        self.boton1.grid(column=0, row=6, padx=4, pady=4)

    def borrar(self):
        datos=(self.carga_dni.get(), )
        cantidad=self.acciones.baja(datos)
        if cantidad==1:
            mb.showinfo("Información","Se ha eliminado el registro!")
        else:
            mb.showinfo("Información","No existe el registro!!")

estudiante = Estudiante()
