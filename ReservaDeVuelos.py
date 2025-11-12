import tkinter as tk
from tkinter import messagebox
import random

# ---------- Datos globales----------
vuelos = []          
MAX_FILAS = 50       
MAX_COLUMNAS = 20    

#----------------------------
#|                          |
#|  OPCION #1- CREAR VUELO  |
#|                          |
#----------------------------
def crear_vuelo():
    ventana_crear = tk.Toplevel(ventana)
    ventana_crear.title("Crear nuevo vuelo")
    ventana_crear.geometry("360x260")
    ventana_crear.configure(bg="lavenderblush")

    etiqueta_filas = tk.Label(ventana_crear, text="Filas (1 a 50):", bg="lavenderblush")
    etiqueta_filas.pack(pady=5)
    entry_filas = tk.Entry(ventana_crear)
    entry_filas.pack()

    etiqueta_columnas = tk.Label(ventana_crear, text="Columnas (1 a 20):", bg="lavenderblush")
    etiqueta_columnas.pack(pady=5)
    entry_columnas = tk.Entry(ventana_crear)
    entry_columnas.pack()

    def confirmar_creacion():
        texto_filas = entry_filas.get().strip()
        texto_columnas = entry_columnas.get().strip()

        if texto_filas == "" or texto_columnas == "":
            messagebox.showerror("Error", "Debes ingresar filas y columnas.")
            return

        try:
            filas_int = int(texto_filas)
            columnas_int = int(texto_columnas)
        except:
            messagebox.showerror("Error", "Filas y columnas deben ser enteros.")
            return

        if filas_int <= 0 or columnas_int <= 0:
            messagebox.showerror("Error", "Filas y columnas deben ser mayor a 0.")
            return

        if filas_int > MAX_FILAS or columnas_int > MAX_COLUMNAS:
            messagebox.showerror(
                "Error",
                f"Tamaño máximo: {MAX_FILAS} filas x {MAX_COLUMNAS} columnas.\n"
                "Puedes usar tamaños menores, nunca mayores."
            )
            return

        # Crear matriz de asientos (0 = libre)
        matriz_asientos = []
        for indice_fila in range(filas_int):
            fila_asientos = []
            for indice_columna in range(columnas_int):
                fila_asientos.append(0)
            matriz_asientos.append(fila_asientos)

        # Agregar vuelo vacío a la lista global
        vuelo_nuevo = ["", "", "", 0.0, matriz_asientos, 0]
        vuelos.append(vuelo_nuevo)

        numero_interno_vuelo = len(vuelos)  # 1,2,3,...
        messagebox.showinfo(
            "Éxito",
            f"¡Vuelo {numero_interno_vuelo} creado exitosamente!\n"
            f"Tamaño: {filas_int} filas x {columnas_int} columnas"
        )
        

        ventana_crear.destroy()

    boton_crear = tk.Button(
        ventana_crear, text="Crear",
        command=confirmar_creacion,
        bg="pink", activebackground="hotpink"
    )
    boton_crear.pack(pady=12)

    boton_cancelar = tk.Button(
        ventana_crear, text="Cancelar",
        command=ventana_crear.destroy,
        bg="light gray"
    )
    boton_cancelar.pack(pady=5)

#------------------------------
#|                            |
#|  OPCION #2- ASIGNAR VUELO  |
#|                            |
#------------------------------

def asignar_datos_vuelo():
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    ventana_asignar = tk.Toplevel(ventana)
    ventana_asignar.title("Asignar datos al vuelo")
    ventana_asignar.geometry("360x320")
    ventana_asignar.configure(bg="lavenderblush")
    
    # Número de vuelo
    etiqueta_vuelo = tk.Label(ventana_asignar, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_asignar)
    entry_vuelo.pack()
    
    # Código de vuelo
    etiqueta_codigo = tk.Label(ventana_asignar, text="Código de vuelo (ej: CMB123):", bg="lavenderblush")
    etiqueta_codigo.pack(pady=5)
    entry_codigo = tk.Entry(ventana_asignar)
    entry_codigo.pack()
    
    # Origen
    etiqueta_origen = tk.Label(ventana_asignar, text="Origen:", bg="lavenderblush")
    etiqueta_origen.pack(pady=5)
    entry_origen = tk.Entry(ventana_asignar)
    entry_origen.pack()
    
    # Destino
    etiqueta_destino = tk.Label(ventana_asignar, text="Destino:", bg="lavenderblush")
    etiqueta_destino.pack(pady=5)
    entry_destino = tk.Entry(ventana_asignar)
    entry_destino.pack()
    
    # Precio
    etiqueta_precio = tk.Label(ventana_asignar, text="Precio del boleto:", bg="lavenderblush")
    etiqueta_precio.pack(pady=5)
    entry_precio = tk.Entry(ventana_asignar)
    entry_precio.pack()
    
    def confirmar_asignacion():
        texto_vuelo = entry_vuelo.get().strip()
        codigo = entry_codigo.get().strip().upper()
        origen = entry_origen.get().strip()
        destino = entry_destino.get().strip()
        texto_precio = entry_precio.get().strip()
        
        if texto_vuelo == "" or codigo == "" or origen == "" or destino == "" or texto_precio == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        indice = num_vuelo - 1
        vuelo = vuelos[indice]
        
        if vuelo[0] != "" or vuelo[1] != "" or vuelo[2] != "":
            messagebox.showerror(
                "Error", 
                f"El vuelo {num_vuelo} ya tiene datos asignados:\n"
                f"Código: {vuelo[0]}\n"
                f"Origen: {vuelo[1]}\n"
                f"Destino: {vuelo[2]}\n\n"
                f"No se puede reasignar."
            )
            return
        
        if len(codigo) != 6:
            messagebox.showerror("Error", "El código debe tener exactamente 6 caracteres (3 letras + 3 números).\nEjemplo: CM123")
            return
        
        if not codigo[:3].isalpha():
            messagebox.showerror("Error", "Los primeros 3 caracteres del código deben ser letras.\nEjemplo: CM123")
            return
        
        if not codigo[3:].isdigit():
            messagebox.showerror("Error", "Los últimos 3 caracteres del código deben ser números.\nEjemplo: CM123")
            return
        
        try:
            precio = float(texto_precio)
            if precio <= 0:
                messagebox.showerror("Error", "El precio debe ser mayor a 0.")
                return
        except:
            messagebox.showerror("Error", "El precio debe ser un número válido.")
            return
        
        vuelos[indice][0] = codigo
        vuelos[indice][1] = origen
        vuelos[indice][2] = destino
        vuelos[indice][3] = precio
        
        messagebox.showinfo(
            "Éxito",
            f"Datos asignados exitosamente al vuelo {num_vuelo}:\n"
            f"Código: {codigo}\n"
            f"Ruta: {origen} → {destino}\n"
            f"Precio: ${precio}"
        )
        ventana_asignar.destroy()
        
    boton_asignar = tk.Button(
        ventana_asignar, text="Asignar",
        command=confirmar_asignacion,
        bg="pink", activebackground="hotpink"
    )
    boton_asignar.pack(pady=12)
    
    boton_cancelar = tk.Button(
        ventana_asignar, text="Cancelar",
        command=ventana_asignar.destroy,
        bg="light gray"
    )
    boton_cancelar.pack(pady=5)


#--------------------------------
#|                              |
#|  OPCION #3- ESTADO DE VUELO  |
#|                              |
#--------------------------------

def ver_estado_vuelo():
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    ventana_estado = tk.Toplevel(ventana)
    ventana_estado.title("Ver estado del vuelo")
    ventana_estado.geometry("400x200")
    ventana_estado.configure(bg="lavenderblush")
    
    etiqueta_vuelo = tk.Label(ventana_estado, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_estado)
    entry_vuelo.pack()
    
    def mostrar_estado():
        texto_vuelo = entry_vuelo.get().strip()
        
        if texto_vuelo == "":
            messagebox.showerror("Error", "Debes ingresar el número de vuelo.")
            return
        
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        indice_vuelo = num_vuelo - 1
        vuelo = vuelos[indice_vuelo]
        
        if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
            messagebox.showerror("Error", "Este vuelo no tiene origen/destino asignado.\nUsa la opción 2 primero.")
            return
        
        codigo = vuelo[0]
        origen = vuelo[1]
        destino = vuelo[2]
        matriz = vuelo[4]
        num_filas = len(matriz)
        num_columnas = len(matriz[0]) if num_filas > 0 else 0
        
        asientos_totales = num_filas * num_columnas
        asientos_ocupados = 0
        for fila in matriz:
            for asiento in fila:
                if asiento == 1:
                    asientos_ocupados = asientos_ocupados + 1
        
        porcentaje = (asientos_ocupados / asientos_totales * 100) if asientos_totales > 0 else 0
        
        ventana_avion = tk.Toplevel(ventana)
        ventana_avion.title(f"Estado del Vuelo {num_vuelo} - {codigo}")
        ventana_avion.configure(bg="lavenderblush")
        
        titulo = tk.Label(ventana_avion,
                         text=f"Vuelo {num_vuelo} - {codigo}\n{origen} → {destino}",
                         bg="lavenderblush",
                         font=("Arial", 12, "bold"),
                         fg="dark slate gray")
        titulo.pack(pady=10)
        
        frame_canvas = tk.Frame(ventana_avion, bg="lavenderblush")
        frame_canvas.pack(pady=10, padx=10)
        
        scrollbar_v = tk.Scrollbar(frame_canvas, orient="vertical")
        scrollbar_h = tk.Scrollbar(frame_canvas, orient="horizontal")
        
        tamano_asiento = 35  #TAMANO DE CADA CUADRITO
        ancho_canvas = min(num_columnas * tamano_asiento + 50, 700)
        alto_canvas = min(num_filas * tamano_asiento + 50, 500)
        
        canvas = tk.Canvas(frame_canvas,
                          width=ancho_canvas,
                          height=alto_canvas,
                          bg="white",
                          yscrollcommand=scrollbar_v.set,
                          xscrollcommand=scrollbar_h.set)
        
        scrollbar_v.config(command=canvas.yview)
        scrollbar_h.config(command=canvas.xview)
        
        scrollbar_v.pack(side="right", fill="y")
        scrollbar_h.pack(side="bottom", fill="x")
        canvas.pack(side="left")
        
        canvas_ancho = num_columnas * tamano_asiento + 50
        canvas_alto = num_filas * tamano_asiento + 50
        canvas.config(scrollregion=(0, 0, canvas_ancho, canvas_alto))
        
        margen_x = 25
        margen_y = 25
        
        for fila in range(num_filas):
            for columna in range(num_columnas):
                x1 = margen_x + columna * tamano_asiento
                y1 = margen_y + fila * tamano_asiento
                x2 = x1 + tamano_asiento - 5
                y2 = y1 + tamano_asiento - 5
                
                if matriz[fila][columna] == 0:
                    color = "#90EE90"  
                    color_borde = "#228B22"  
                else:
                    color = "#FFB6C6"  # R
                    color_borde = "#DC143C"  
                
                canvas.create_rectangle(x1, y1, x2, y2,
                                       fill=color,
                                       outline=color_borde,
                                       width=2)
                
                letra_fila = chr(fila + ord('A'))
                numero_columna = columna + 1
                etiqueta = f"{letra_fila}{numero_columna}"
                
                centro_x = (x1 + x2) / 2
                centro_y = (y1 + y2) / 2
                canvas.create_text(centro_x, centro_y,
                                  text=etiqueta,
                                  font=("Arial", 8, "bold"),
                                  fill="black")
        
        leyenda_y = margen_y + num_filas * tamano_asiento + 15
        
        canvas.create_rectangle(margen_x, leyenda_y, margen_x + 20, leyenda_y + 20,
                               fill="#90EE90", outline="#228B22", width=2)
        canvas.create_text(margen_x + 30, leyenda_y + 10,
                          text="Libre", anchor="w", font=("Arial", 9))
        
        canvas.create_rectangle(margen_x + 80, leyenda_y, margen_x + 100, leyenda_y + 20,
                               fill="#FFB6C6", outline="#DC143C", width=2)
        canvas.create_text(margen_x + 110, leyenda_y + 10,
                          text="Ocupado", anchor="w", font=("Arial", 9))
        
        frame_stats = tk.Frame(ventana_avion, bg="mistyrose", bd=2, relief="solid")
        frame_stats.pack(pady=10, padx=20, fill="x")
        
        stats_texto = f"Asientos totales: {asientos_totales}  |  " \
                     f"Ocupados: {asientos_ocupados}  |  " \
                     f"Libres: {asientos_totales - asientos_ocupados}  |  " \
                     f"Ocupación: {porcentaje:.2f}%"
        
        label_stats = tk.Label(frame_stats,
                              text=stats_texto,
                              bg="mistyrose",
                              font=("Arial", 10, "bold"),
                              fg="dark slate gray",
                              pady=8)
        label_stats.pack()
        
        boton_cerrar = tk.Button(ventana_avion,
                                text="Cerrar",
                                command=ventana_avion.destroy,
                                bg="light gray",
                                width=15)
        boton_cerrar.pack(pady=10)
        
        ventana_estado.destroy()
    
    boton_mostrar = tk.Button(
        ventana_estado, text="Ver Estado",
        command=mostrar_estado,
        bg="pink", activebackground="hotpink"
    )
    boton_mostrar.pack(pady=12)
    
    boton_cerrar = tk.Button(
        ventana_estado, text="Cerrar",
        command=ventana_estado.destroy,
        bg="light gray"
    )
    boton_cerrar.pack(pady=5)


def reservar_asiento():
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    ventana_reservar = tk.Toplevel(ventana)
    ventana_reservar.title("Reservar asiento")
    ventana_reservar.geometry("360x260")
    ventana_reservar.configure(bg="lavenderblush")
    
    # Número de vuelo
    etiqueta_vuelo = tk.Label(ventana_reservar, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_reservar)
    entry_vuelo.pack()
    
    # Letra de fila
    etiqueta_fila = tk.Label(ventana_reservar, text="Letra de fila (ej: A, B, C...):", bg="lavenderblush")
    etiqueta_fila.pack(pady=5)
    entry_fila = tk.Entry(ventana_reservar)
    entry_fila.pack()
    
    # Número de columna
    etiqueta_columna = tk.Label(ventana_reservar, text="Número de columna (ej: 1, 2, 3...):", bg="lavenderblush")
    etiqueta_columna.pack(pady=5)
    entry_columna = tk.Entry(ventana_reservar)
    entry_columna.pack()
    
    def confirmar_reserva():
    
        texto_vuelo = entry_vuelo.get().strip()
        letra_fila = entry_fila.get().strip().upper()  # Convertir a mayúscula
        texto_columna = entry_columna.get().strip()
        
        if texto_vuelo == "" or letra_fila == "" or texto_columna == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        indice_vuelo = num_vuelo - 1
        vuelo = vuelos[indice_vuelo]
        
        if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
            messagebox.showerror("Error", "Este vuelo no tiene origen/destino asignado.\nUsa la opción 2 primero.")
            return
        
        if len(letra_fila) != 1 or not letra_fila.isalpha():
            messagebox.showerror("Error", "La fila debe ser una sola letra (A, B, C...).")
            return
        
        indice_fila = ord(letra_fila) - ord('A')
        
        try:
            num_columna = int(texto_columna)
        except:
            messagebox.showerror("Error", "La columna debe ser un número.")
            return
        
        if num_columna < 1:
            messagebox.showerror("Error", "La columna debe ser mayor o igual a 1.")
            return
        
        indice_columna = num_columna - 1
        
        matriz = vuelo[4]
        num_filas = len(matriz)
        num_columnas = len(matriz[0]) if num_filas > 0 else 0
        
        if indice_fila < 0 or indice_fila >= num_filas:
            messagebox.showerror("Error", f"La fila {letra_fila} no existe.\nEste vuelo tiene filas de A hasta {chr(num_filas - 1 + ord('A'))}.")
            return
        
        if indice_columna < 0 or indice_columna >= num_columnas:
            messagebox.showerror("Error", f"La columna {num_columna} no existe.\nEste vuelo tiene columnas de 1 hasta {num_columnas}.")
            return
        
        if matriz[indice_fila][indice_columna] == 1:
            messagebox.showerror("Error", f"El asiento {letra_fila}{num_columna} ya está ocupado.")
            return
        
        matriz[indice_fila][indice_columna] = 1
        vuelo[5] += 1  # Incrementar contador de vendidos
        
        codigo = vuelo[0]
        origen = vuelo[1]
        destino = vuelo[2]
        
        messagebox.showinfo(
            "Éxito",
            f"¡Asiento reservado exitosamente!\n\n"
            f"Vuelo {num_vuelo} - {codigo}\n"
            f"{origen} → {destino}\n"
            f"Asiento: {letra_fila}{num_columna}"
        )
        ventana_reservar.destroy()
    
    boton_reservar = tk.Button(
        ventana_reservar, text="Reservar",
        command=confirmar_reserva,
        bg="pink", activebackground="hotpink"
    )
    boton_reservar.pack(pady=12)
    
    boton_cancelar = tk.Button(
        ventana_reservar, text="Cancelar",
        command=ventana_reservar.destroy,
        bg="light gray"
    )
    boton_cancelar.pack(pady=5)

def cancelar_reserva():
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    ventana_cancelar = tk.Toplevel(ventana)
    ventana_cancelar.title("Cancelar reserva")
    ventana_cancelar.geometry("360x260")
    ventana_cancelar.configure(bg="lavenderblush")
    
    #Número de vuelo
    etiqueta_vuelo = tk.Label(ventana_cancelar, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_cancelar)
    entry_vuelo.pack()
    
    #Letra de fila
    etiqueta_fila = tk.Label(ventana_cancelar, text="Letra de fila (ej: A, B, C...):", bg="lavenderblush")
    etiqueta_fila.pack(pady=5)
    entry_fila = tk.Entry(ventana_cancelar)
    entry_fila.pack()
    
    #Número de columna
    etiqueta_columna = tk.Label(ventana_cancelar, text="Número de columna (ej: 1, 2, 3...):", bg="lavenderblush")
    etiqueta_columna.pack(pady=5)
    entry_columna = tk.Entry(ventana_cancelar)
    entry_columna.pack()
    
    def confirmar_cancelacion():
        texto_vuelo = entry_vuelo.get().strip()
        letra_fila = entry_fila.get().strip().upper()  
        texto_columna = entry_columna.get().strip()
        
        if texto_vuelo == "" or letra_fila == "" or texto_columna == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        indice_vuelo = num_vuelo - 1  
        vuelo = vuelos[indice_vuelo]
        
        if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
            messagebox.showerror("Error", "Este vuelo no tiene origen/destino asignado.\nUsa la opción 2 primero.")
            return
        
        if len(letra_fila) != 1 or not letra_fila.isalpha():
            messagebox.showerror("Error", "La fila debe ser una sola letra (A, B, C...).")
            return
        
        indice_fila = ord(letra_fila) - ord('A')
        
        try:
            num_columna = int(texto_columna)
        except:
            messagebox.showerror("Error", "La columna debe ser un número.")
            return
        
        if num_columna < 1:
            messagebox.showerror("Error", "La columna debe ser mayor o igual a 1.")
            return
        
        indice_columna = num_columna - 1
        
        matriz = vuelo[4]
        num_filas = len(matriz)
        num_columnas = len(matriz[0]) if num_filas > 0 else 0
        
        if indice_fila < 0 or indice_fila >= num_filas:
            messagebox.showerror("Error", f"La fila {letra_fila} no existe.\nEste vuelo tiene filas de A hasta {chr(num_filas - 1 + ord('A'))}.")
            return
        
        if indice_columna < 0 or indice_columna >= num_columnas:
            messagebox.showerror("Error", f"La columna {num_columna} no existe.\nEste vuelo tiene columnas de 1 hasta {num_columnas}.")
            return
        
        if matriz[indice_fila][indice_columna] == 0:
            messagebox.showerror("Error", f"El asiento {letra_fila}{num_columna} ya está libre.\nNo hay nada que cancelar.")
            return
        
        matriz[indice_fila][indice_columna] = 0
        vuelo[5] = vuelo[5] - 1  

        messagebox.showinfo(
            "Éxito",
            f"¡Reserva del asiento {letra_fila}{num_columna} cancelada!"
        )
        ventana_cancelar.destroy()
    
    boton_cancelar_reserva = tk.Button(
        ventana_cancelar, text="Cancelar Reserva",
        command=confirmar_cancelacion,
        bg="pink", activebackground="hotpink"
    )
    boton_cancelar_reserva.pack(pady=12)
    
    boton_cerrar = tk.Button(
        ventana_cancelar, text="Cerrar",
        command=ventana_cancelar.destroy,
        bg="light gray"
    )
    boton_cerrar.pack(pady=5)


def ver_estadisticas_ocupacion():
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    ventana_stats = tk.Toplevel(ventana)
    ventana_stats.title("Estadísticas de ocupación")
    ventana_stats.geometry("360x180")
    ventana_stats.configure(bg="lavenderblush")
    
    #Número de vuelo
    etiqueta_vuelo = tk.Label(ventana_stats, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_stats)
    entry_vuelo.pack()
    
    def mostrar_estadisticas():
        texto_vuelo = entry_vuelo.get().strip()
        
        if texto_vuelo == "":
            messagebox.showerror("Error", "Debes ingresar el número de vuelo.")
            return
        
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        indice_vuelo = num_vuelo - 1
        vuelo = vuelos[indice_vuelo]
        
        if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
            messagebox.showerror("Error", "Este vuelo no tiene origen/destino asignado.\nUsa la opción 2 primero.")
            return
        
        # Paso 7: Obtener datos del vuelo
        codigo = vuelo[0]
        origen = vuelo[1]
        destino = vuelo[2]
        matriz = vuelo[4]
        
        # Paso 8: Calcular asientos totales
        num_filas = len(matriz)
        num_columnas = len(matriz[0]) if num_filas > 0 else 0
        asientos_totales = num_filas * num_columnas
        
        # Paso 9: Contar asientos reservados (contar los 1 en la matriz)
        asientos_reservados = 0
        for fila in matriz:
            for asiento in fila:
                if asiento == 1:
                    asientos_reservados = asientos_reservados + 1
        
        # Paso 10: Calcular porcentaje de ocupación
        if asientos_totales > 0:
            porcentaje = (asientos_reservados / asientos_totales) * 100
        else:
            porcentaje = 0
        
        # Paso 11: Mostrar resultados
        mensaje = f"Vuelo {num_vuelo} - {codigo} {origen} → {destino}\n\n"
        mensaje = mensaje + f"Asientos totales: {asientos_totales}\n"
        mensaje = mensaje + f"Reservados: {asientos_reservados}\n"
        mensaje = mensaje + f"Porcentaje de ocupación: {porcentaje:.2f}%"
        
        messagebox.showinfo("Estadísticas de ocupación", mensaje)
    
    # Botón para mostrar
    boton_mostrar = tk.Button(
        ventana_stats, text="Ver Estadísticas",
        command=mostrar_estadisticas,
        bg="pink", activebackground="hotpink"
    )
    boton_mostrar.pack(pady=12)
    
    # Botón para cerrar
    boton_cerrar = tk.Button(
        ventana_stats, text="Cerrar",
        command=ventana_stats.destroy,
        bg="light gray"
    )
    boton_cerrar.pack(pady=5)


def ver_estadisticas_recaudacion():
    # Verificar que hay vuelos
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    # Crear ventana nueva
    ventana_recaudacion = tk.Toplevel(ventana)
    ventana_recaudacion.title("Estadísticas de recaudación")
    ventana_recaudacion.geometry("360x180")
    ventana_recaudacion.configure(bg="lavenderblush")
    
    # Campo: Número de vuelo
    etiqueta_vuelo = tk.Label(ventana_recaudacion, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_recaudacion)
    entry_vuelo.pack()
    
    def mostrar_recaudacion():
        # Paso 1: Obtener el número de vuelo
        texto_vuelo = entry_vuelo.get().strip()
        
        # Paso 2: Validar que no esté vacío
        if texto_vuelo == "":
            messagebox.showerror("Error", "Debes ingresar el número de vuelo.")
            return
        
        # Paso 3: Validar que sea un número
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        # Paso 4: Verificar que el vuelo existe
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        # Paso 5: Obtener el vuelo
        indice_vuelo = num_vuelo - 1
        vuelo = vuelos[indice_vuelo]
        
        # Paso 6: Verificar que el vuelo tenga datos asignados
        if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
            messagebox.showerror("Error", "Este vuelo no tiene origen/destino asignado.\nUsa la opción 2 primero.")
            return
        
        # Paso 7: Obtener datos del vuelo
        codigo = vuelo[0]
        origen = vuelo[1]
        destino = vuelo[2]
        precio = vuelo[3]
        entradas_vendidas = vuelo[5]
        
        # Paso 8: Calcular total recaudado
        total_recaudado = entradas_vendidas * precio
        
        # Paso 9: Mostrar resultados
        mensaje = f"Vuelo {num_vuelo} - {codigo} {origen} → {destino}\n\n"
        mensaje = mensaje + f"Entradas vendidas: {entradas_vendidas}\n"
        mensaje = mensaje + f"Precio por boleto: {precio}\n"
        mensaje = mensaje + f"Total recaudado: {total_recaudado}"
        
        messagebox.showinfo("Estadísticas de recaudación", mensaje)
    
    # Botón para mostrar
    boton_mostrar = tk.Button(
        ventana_recaudacion, text="Ver Recaudación",
        command=mostrar_recaudacion,
        bg="pink", activebackground="hotpink"
    )
    boton_mostrar.pack(pady=12)
    
    # Botón para cerrar
    boton_cerrar = tk.Button(
        ventana_recaudacion, text="Cerrar",
        command=ventana_recaudacion.destroy,
        bg="light gray"
    )
    boton_cerrar.pack(pady=5)

def buscar_vuelos_por_destino():
    # Verificar que hay vuelos
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    # Crear ventana nueva
    ventana_buscar = tk.Toplevel(ventana)
    ventana_buscar.title("Buscar vuelos por destino")
    ventana_buscar.geometry("550x600")
    ventana_buscar.configure(bg="lavenderblush")
    
    # Título
    etiqueta_titulo = tk.Label(ventana_buscar, text="Selecciona un destino:", 
                               bg="lavenderblush", font=("Arial", 11, "bold"))
    etiqueta_titulo.pack(pady=10)
    
    # Obtener lista de destinos únicos
    destinos_unicos = []
    for vuelo in vuelos:
        destino = vuelo[2]
        # Solo agregar destinos que tengan datos y no estén repetidos
        if destino != "" and destino not in destinos_unicos:
            destinos_unicos.append(destino)
    
    # Si no hay destinos
    if len(destinos_unicos) == 0:
        etiqueta_sin_datos = tk.Label(ventana_buscar, 
                                      text="No hay vuelos con destinos asignados.\nUsa la opción 2 primero.",
                                      bg="lavenderblush", fg="red")
        etiqueta_sin_datos.pack(pady=20)
        
        boton_cerrar = tk.Button(ventana_buscar, text="Cerrar",
                                command=ventana_buscar.destroy,
                                bg="light gray")
        boton_cerrar.pack(pady=10)
        return
    
    # Crear Listbox para mostrar destinos
    frame_lista = tk.Frame(ventana_buscar, bg="lavenderblush")
    frame_lista.pack(pady=10)
    
    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side="right", fill="y")
    
    listbox_destinos = tk.Listbox(frame_lista, width=40, height=8,
                                   yscrollcommand=scrollbar.set,
                                   font=("Arial", 10))
    listbox_destinos.pack(side="left")
    scrollbar.config(command=listbox_destinos.yview)
    
    # Agregar destinos al Listbox
    for destino in destinos_unicos:
        listbox_destinos.insert("end", destino)
    
    # Área de texto para mostrar resultados
    etiqueta_resultados = tk.Label(ventana_buscar, text="Resultados:",
                                   bg="lavenderblush", font=("Arial", 10, "bold"))
    etiqueta_resultados.pack(pady=(10, 5))
    
    texto_resultados = tk.Text(ventana_buscar, width=50, height=8,
                              bg="white", fg="black", font=("Arial", 9))
    texto_resultados.pack(pady=5, padx=10)
    texto_resultados.config(state="disabled")
    
    def mostrar_vuelos_destino():
        # Obtener selección
        seleccion = listbox_destinos.curselection()
        
        if len(seleccion) == 0:
            messagebox.showwarning("Advertencia", "Debes seleccionar un destino de la lista.")
            return
        
        # Obtener el destino seleccionado
        indice_seleccion = seleccion[0]
        destino_seleccionado = destinos_unicos[indice_seleccion]
        
        # Buscar vuelos con ese destino
        vuelos_encontrados = []
        
        for indice in range(len(vuelos)):
            vuelo = vuelos[indice]
            destino_vuelo = vuelo[2]
            
            if destino_vuelo == destino_seleccionado:
                # Calcular asientos disponibles
                matriz = vuelo[4]
                asientos_disponibles = 0
                
                for fila in matriz:
                    for asiento in fila:
                        if asiento == 0:
                            asientos_disponibles = asientos_disponibles + 1
                
                num_vuelo = indice + 1
                vuelos_encontrados.append([num_vuelo, asientos_disponibles])
        
        # Mostrar resultados en el Text widget
        texto_resultados.config(state="normal")
        texto_resultados.delete("1.0", "end")
        
        mensaje = f"Destino: {destino_seleccionado}\n\n"
        mensaje = mensaje + f"Vuelos hacia \"{destino_seleccionado}\":\n\n"
        
        for vuelo_info in vuelos_encontrados:
            num = vuelo_info[0]
            disponibles = vuelo_info[1]
            mensaje = mensaje + f"  • Vuelo {num} (asientos disponibles: {disponibles})\n"
        
        texto_resultados.insert("1.0", mensaje)
        texto_resultados.config(state="disabled")
    
    # Botón para buscar
    boton_buscar = tk.Button(ventana_buscar, text="Ver Vuelos",
                            command=mostrar_vuelos_destino,
                            bg="pink", activebackground="hotpink",
                            width=15)
    boton_buscar.pack(pady=10)
    
    # Botón para cerrar
    boton_cerrar = tk.Button(ventana_buscar, text="Cerrar",
                            command=ventana_buscar.destroy,
                            bg="light gray", width=15)
    boton_cerrar.pack(pady=5)

def ver_vuelos_disponibles():
    # Verificar que hay vuelos
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    # Crear ventana nueva con scroll
    ventana_vuelos = tk.Toplevel(ventana)
    ventana_vuelos.title("Vuelos disponibles")
    ventana_vuelos.geometry("500x400")
    ventana_vuelos.configure(bg="lavenderblush")
    
    # Crear un Text widget para mostrar múltiples vuelos
    texto = tk.Text(ventana_vuelos, width=60, height=20, bg="white", fg="black")
    texto.pack(pady=10, padx=10)
    
    # Construir la lista de vuelos
    mensaje = "--- Vuelos disponibles ---\n\n"
    vuelos_con_datos = 0  # Contador de vuelos que tienen datos
    
    # Recorrer todos los vuelos
    for indice in range(len(vuelos)):
        vuelo = vuelos[indice]
        codigo = vuelo[0]
        origen = vuelo[1]
        destino = vuelo[2]
        precio = vuelo[3]
        matriz = vuelo[4]
        
        # Solo mostrar vuelos que tengan datos asignados
        if codigo != "" and origen != "" and destino != "":
            vuelos_con_datos = vuelos_con_datos + 1
            
            # Calcular asientos totales
            num_filas = len(matriz)
            num_columnas = len(matriz[0]) if num_filas > 0 else 0
            asientos_totales = num_filas * num_columnas
            
            # Contar asientos libres (los que tienen 0)
            asientos_libres = 0
            for fila in matriz:
                for asiento in fila:
                    if asiento == 0:
                        asientos_libres = asientos_libres + 1
            
            # Agregar información del vuelo al mensaje
            num_vuelo = indice + 1
            mensaje = mensaje + f"Vuelo {num_vuelo} - {codigo} {origen} → {destino}\n"
            mensaje = mensaje + f"Precio: {precio}\n"
            mensaje = mensaje + f"Asientos disponibles: {asientos_libres}\n\n"
    
    # Si no hay vuelos con datos asignados
    if vuelos_con_datos == 0:
        mensaje = "No hay vuelos con datos asignados.\n"
        mensaje = mensaje + "Usa la opción 2 para asignar origen/destino a los vuelos."
    
    # Mostrar el mensaje en el Text widget
    texto.insert("1.0", mensaje)
    texto.config(state="disabled")  # Hacer que no se pueda editar
    
    # Botón para cerrar
    boton_cerrar = tk.Button(
        ventana_vuelos, text="Cerrar",
        command=ventana_vuelos.destroy,
        bg="light gray"
    )
    boton_cerrar.pack(pady=5)

def reservar_asientos_consecutivos():
    # Verificar que hay vuelos
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    # Crear ventana nueva
    ventana_consecutivos = tk.Toplevel(ventana)
    ventana_consecutivos.title("Reservar asientos consecutivos")
    ventana_consecutivos.geometry("360x300")
    ventana_consecutivos.configure(bg="lavenderblush")
    
    # Campo: Número de vuelo
    etiqueta_vuelo = tk.Label(ventana_consecutivos, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_consecutivos)
    entry_vuelo.pack()
    
    # Campo: Letra de fila
    etiqueta_fila = tk.Label(ventana_consecutivos, text="Letra de fila (ej: A, B, C...):", bg="lavenderblush")
    etiqueta_fila.pack(pady=5)
    entry_fila = tk.Entry(ventana_consecutivos)
    entry_fila.pack()
    
    # Campo: Columna inicial
    etiqueta_columna = tk.Label(ventana_consecutivos, text="Columna inicial (ej: 1, 2, 3...):", bg="lavenderblush")
    etiqueta_columna.pack(pady=5)
    entry_columna = tk.Entry(ventana_consecutivos)
    entry_columna.pack()
    
    # Campo: Cantidad de asientos
    etiqueta_cantidad = tk.Label(ventana_consecutivos, text="Cantidad de asientos:", bg="lavenderblush")
    etiqueta_cantidad.pack(pady=5)
    entry_cantidad = tk.Entry(ventana_consecutivos)
    entry_cantidad.pack()
    
    def confirmar_reserva_consecutiva():
        # Paso 1: Obtener valores
        texto_vuelo = entry_vuelo.get().strip()
        letra_fila = entry_fila.get().strip().upper()
        texto_columna = entry_columna.get().strip()
        texto_cantidad = entry_cantidad.get().strip()
        
        # Paso 2: Validar que no estén vacíos
        if texto_vuelo == "" or letra_fila == "" or texto_columna == "" or texto_cantidad == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        # Paso 3: Validar número de vuelo
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        # Paso 4: Obtener el vuelo
        indice_vuelo = num_vuelo - 1
        vuelo = vuelos[indice_vuelo]
        
        # Verificar que el vuelo tenga datos
        if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
            messagebox.showerror("Error", "Este vuelo no tiene origen/destino asignado.\nUsa la opción 2 primero.")
            return
        
        # Paso 5: Validar letra de fila
        if len(letra_fila) != 1 or not letra_fila.isalpha():
            messagebox.showerror("Error", "La fila debe ser una sola letra (A, B, C...).")
            return
        
        # Convertir letra a índice
        indice_fila = ord(letra_fila) - ord('A')
        
        # Paso 6: Validar columna inicial
        try:
            columna_inicial = int(texto_columna)
        except:
            messagebox.showerror("Error", "La columna debe ser un número.")
            return
        
        if columna_inicial < 1:
            messagebox.showerror("Error", "La columna debe ser mayor o igual a 1.")
            return
        
        # Paso 7: Validar cantidad
        try:
            cantidad = int(texto_cantidad)
        except:
            messagebox.showerror("Error", "La cantidad debe ser un número.")
            return
        
        if cantidad < 1:
            messagebox.showerror("Error", "La cantidad debe ser mayor o igual a 1.")
            return
        
        # Paso 8: Obtener matriz
        matriz = vuelo[4]
        num_filas = len(matriz)
        num_columnas = len(matriz[0]) if num_filas > 0 else 0
        
        # Validar que la fila existe
        if indice_fila < 0 or indice_fila >= num_filas:
            messagebox.showerror("Error", f"La fila {letra_fila} no existe.\nEste vuelo tiene filas de A hasta {chr(num_filas - 1 + ord('A'))}.")
            return
        
        # Paso 9: Verificar que todos los asientos consecutivos existen y están libres
        indice_columna_inicial = columna_inicial - 1
        
        # Lista para guardar los asientos a reservar
        asientos_a_reservar = []
        
        for i in range(cantidad):
            indice_columna = indice_columna_inicial + i
            
            # Verificar que la columna existe
            if indice_columna >= num_columnas:
                messagebox.showerror("Error", f"No hay suficientes asientos consecutivos.\nLa fila solo tiene {num_columnas} columnas.")
                return
            
            # Verificar que el asiento está libre
            if matriz[indice_fila][indice_columna] == 1:
                numero_columna = indice_columna + 1
                messagebox.showerror("Error", f"No es posible reservar los asientos consecutivos.\nEl asiento {letra_fila}{numero_columna} está ocupado.")
                return
            
            # Guardar el asiento
            asientos_a_reservar.append(indice_columna)
        
        # Paso 10: Si llegamos aquí, todos los asientos están libres, reservarlos
        asientos_reservados_texto = ""
        
        for indice_columna in asientos_a_reservar:
            matriz[indice_fila][indice_columna] = 1
            vuelo[5] = vuelo[5] + 1
            numero_columna = indice_columna + 1
            asientos_reservados_texto = asientos_reservados_texto + f"{letra_fila}{numero_columna} "
        
        # Paso 11: Mostrar éxito
        messagebox.showinfo(
            "Éxito",
            f"¡Reservados exitosamente: {asientos_reservados_texto}!"
        )
        ventana_consecutivos.destroy()
    
    # Botón para reservar
    boton_reservar = tk.Button(
        ventana_consecutivos, text="Reservar",
        command=confirmar_reserva_consecutiva,
        bg="pink", activebackground="hotpink"
    )
    boton_reservar.pack(pady=12)
    
    # Botón para cancelar
    boton_cancelar = tk.Button(
        ventana_consecutivos, text="Cancelar",
        command=ventana_consecutivos.destroy,
        bg="light gray"
    )
    boton_cancelar.pack(pady=5)

def simular_venta_masiva():
    # Verificar que hay vuelos
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    # Crear ventana nueva
    ventana_simular = tk.Toplevel(ventana)
    ventana_simular.title("Simular venta masiva")
    ventana_simular.geometry("360x180")
    ventana_simular.configure(bg="lavenderblush")
    
    # Campo: Porcentaje
    etiqueta_porcentaje = tk.Label(ventana_simular, text="Porcentaje de ocupación (1 a 100):", bg="lavenderblush")
    etiqueta_porcentaje.pack(pady=5)
    entry_porcentaje = tk.Entry(ventana_simular)
    entry_porcentaje.pack()
    
    def confirmar_simulacion():
        # Paso 1: Obtener el porcentaje
        texto_porcentaje = entry_porcentaje.get().strip()
        
        # Paso 2: Validar que no esté vacío
        if texto_porcentaje == "":
            messagebox.showerror("Error", "Debes ingresar un porcentaje.")
            return
        
        # Paso 3: Validar que sea un número
        try:
            porcentaje = int(texto_porcentaje)
        except:
            messagebox.showerror("Error", "El porcentaje debe ser un número entero.")
            return
        
        # Paso 4: Validar rango (1 a 100)
        if porcentaje < 1 or porcentaje > 100:
            messagebox.showerror("Error", "El porcentaje debe estar entre 1 y 100.")
            return
        
        # Necesitamos importar random al inicio del archivo
        import random
        
        # Paso 5: Recorrer cada vuelo y simular reservas
        for vuelo in vuelos:
            # Solo procesar vuelos con datos asignados
            if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
                continue
            
            matriz = vuelo[4]
            num_filas = len(matriz)
            num_columnas = len(matriz[0]) if num_filas > 0 else 0
            asientos_totales = num_filas * num_columnas
            
            # Calcular cuántos asientos deben estar ocupados
            asientos_objetivo = int((porcentaje / 100.0) * asientos_totales)
            
            # Contar cuántos ya están ocupados
            asientos_ocupados = 0
            for fila in matriz:
                for asiento in fila:
                    if asiento == 1:
                        asientos_ocupados = asientos_ocupados + 1
            
            # Si ya tiene más del porcentaje, no hacer nada
            if asientos_ocupados >= asientos_objetivo:
                continue
            
            # Calcular cuántos asientos faltan por reservar
            asientos_a_reservar = asientos_objetivo - asientos_ocupados
            
            # Crear lista de asientos libres
            asientos_libres = []
            for fila in range(num_filas):
                for columna in range(num_columnas):
                    if matriz[fila][columna] == 0:
                        asientos_libres.append([fila, columna])
            
            # Mezclar la lista aleatoriamente
            random.shuffle(asientos_libres)
            
            # Reservar los primeros N asientos de la lista mezclada
            reservados = 0
            for i in range(len(asientos_libres)):
                if reservados >= asientos_a_reservar:
                    break
                
                fila = asientos_libres[i][0]
                columna = asientos_libres[i][1]
                matriz[fila][columna] = 1
                vuelo[5] = vuelo[5] + 1
                reservados = reservados + 1
        
        # Paso 6: Mostrar mensaje de éxito
        messagebox.showinfo(
            "Éxito",
            f"Simulación completada.\n\n"
            f"Se han reservado asientos aleatoriamente\n"
            f"hasta alcanzar el {porcentaje}% de ocupación\n"
            f"en todos los vuelos.\n\n"
            f"Verifica el resultado con las opciones 3 o 6."
        )
        ventana_simular.destroy()
    
    # Botón para simular
    boton_simular = tk.Button(
        ventana_simular, text="Simular",
        command=confirmar_simulacion,
        bg="pink", activebackground="hotpink"
    )
    boton_simular.pack(pady=12)
    
    # Botón para cancelar
    boton_cancelar = tk.Button(
        ventana_simular, text="Cancelar",
        command=ventana_simular.destroy,
        bg="light gray"
    )
    boton_cancelar.pack(pady=5)

def reiniciar_vuelo():
    # Verificar que hay vuelos
    if len(vuelos) == 0:
        messagebox.showerror("Error", "No hay vuelos creados. Crea un vuelo primero.")
        return
    
    # Crear ventana nueva
    ventana_reiniciar = tk.Toplevel(ventana)
    ventana_reiniciar.title("Reiniciar vuelo")
    ventana_reiniciar.geometry("360x150")
    ventana_reiniciar.configure(bg="lavenderblush")
    
    # Campo: Número de vuelo
    etiqueta_vuelo = tk.Label(ventana_reiniciar, text=f"Número de vuelo (1 a {len(vuelos)}):", bg="lavenderblush")
    etiqueta_vuelo.pack(pady=5)
    entry_vuelo = tk.Entry(ventana_reiniciar)
    entry_vuelo.pack()
    
    def confirmar_reinicio():
        # Paso 1: Obtener el número de vuelo
        texto_vuelo = entry_vuelo.get().strip()
        
        # Paso 2: Validar que no esté vacío
        if texto_vuelo == "":
            messagebox.showerror("Error", "Debes ingresar el número de vuelo.")
            return
        
        # Paso 3: Validar que sea un número
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        # Paso 4: Verificar que el vuelo existe
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        # Paso 5: Obtener el vuelo
        indice_vuelo = num_vuelo - 1
        vuelo = vuelos[indice_vuelo]
        matriz = vuelo[4]
        
        # Paso 6: Reiniciar todos los asientos (ponerlos en 0)
        for fila in range(len(matriz)):
            for columna in range(len(matriz[0])):
                matriz[fila][columna] = 0
        
        # Paso 7: Reiniciar contador de ventas
        vuelo[5] = 0
        
        # Paso 8: Mostrar mensaje de éxito
        messagebox.showinfo(
            "Éxito",
            f"El vuelo {num_vuelo} ha sido reiniciado exitosamente.\n\n"
            f"Todos los asientos están ahora libres."
        )
        ventana_reiniciar.destroy()
    
    # Botón para reiniciar
    boton_reiniciar = tk.Button(
        ventana_reiniciar, text="Reiniciar",
        command=confirmar_reinicio,
        bg="pink", activebackground="hotpink"
    )
    boton_reiniciar.pack(pady=12)
    
    # Botón para cancelar
    boton_cancelar = tk.Button(
        ventana_reiniciar, text="Cancelar",
        command=ventana_reiniciar.destroy,
        bg="light gray"
    )
    boton_cancelar.pack(pady=5)


# --- Ventana principal---
ventana = tk.Tk()
ventana.title("Sistema de Reservas de Vuelos")
ventana.geometry("350x550")
ventana.configure(bg="lavenderblush")  

# --- Paneles ---
panel_menu = tk.Frame(ventana, bd=1, relief="solid", bg="mistyrose") 
panel_menu.pack(fill="both", expand=True)

# --- Título ---
titulo_menu = tk.Label(panel_menu,
                      text="Sistema de Reservas de Vuelos",
                      font=("Arial", 15, "bold"),
                      bg="mistyrose", fg="dark slate gray")
titulo_menu.pack(pady=20)

# --- Frame para centrar botones ---
frame_botones = tk.Frame(panel_menu, bg="mistyrose")
frame_botones.pack(expand=True)

# --- BOTONES ---
boton1 = tk.Button(frame_botones, text="1. Crear nuevo vuelo", width=34,
                 command=crear_vuelo,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton1.pack(pady=5)

boton2 = tk.Button(frame_botones, text="2. Asignar origen/destino y precio a vuelo", width=34,
                 command=asignar_datos_vuelo,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton2.pack(pady=5)

boton3 = tk.Button(frame_botones, text="3. Ver estado de un vuelo", width=34,
                 command=ver_estado_vuelo, 
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton3.pack(pady=5)

boton4 = tk.Button(frame_botones, text="4. Reservar asiento", width=34,
                 command=reservar_asiento,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton4.pack(pady=5)

boton5 = tk.Button(frame_botones, text="5. Cancelar reserva", width=34,
                 command=cancelar_reserva,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton5.pack(pady=5)

boton6 = tk.Button(frame_botones, text="6. Ver estadísticas de ocupación", width=34,
                 command=ver_estadisticas_ocupacion,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton6.pack(pady=5)

boton7 = tk.Button(frame_botones, text="7. Ver estadísticas de recaudación", width=34,
                 command=ver_estadisticas_recaudacion,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton7.pack(pady=5)

boton8 = tk.Button(frame_botones, text="8. Buscar vuelos por destino", width=34,
                 command=buscar_vuelos_por_destino,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton8.pack(pady=5)

boton9 = tk.Button(frame_botones, text="9. Ver vuelos disponibles", width=34,
                 command=ver_vuelos_disponibles,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton9.pack(pady=5)

boton10 = tk.Button(frame_botones, text="10. Reservar varios asientos consecutivos", width=34,
                  command=reservar_asientos_consecutivos,
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton10.pack(pady=5)

boton11 = tk.Button(frame_botones, text="11. Simular venta masiva", width=34,
                  command=simular_venta_masiva,
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton11.pack(pady=5)

boton12 = tk.Button(frame_botones, text="12. Reiniciar vuelo", width=34,
                  command=reiniciar_vuelo,
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton12.pack(pady=5)

boton13 = tk.Button(frame_botones, text="13. Salir", width=34,
                  command=ventana.destroy,
                  bg="white", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton13.pack(pady=12)

# --- Iniciar app ---
ventana.mainloop()
