import tkinter as tk
from tkinter import messagebox



# ---------- Datos ----------
# Cada vuelo: [codigo, origen, destino, precio, matriz_asientos, cantidad_vendidos]
vuelos = []          #lista global de vuelos
MAX_FILAS = 50       
MAX_COLUMNAS = 20    

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
        # [codigo, origen, destino, precio, matriz_asientos, cantidad_vendidos]
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
    etiqueta_codigo = tk.Label(ventana_asignar, text="Código de vuelo (ej: CM123):", bg="lavenderblush")
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
        # Obtener valores
        texto_vuelo = entry_vuelo.get().strip()
        codigo = entry_codigo.get().strip().upper()  # <-- Convertir a mayúsculas
        origen = entry_origen.get().strip()
        destino = entry_destino.get().strip()
        texto_precio = entry_precio.get().strip()
        
        # Validar que no estén vacíos
        if texto_vuelo == "" or codigo == "" or origen == "" or destino == "" or texto_precio == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        # Validar formato del código (3 letras + 3 números)
        if len(codigo) != 6:
            messagebox.showerror("Error", "El código debe tener exactamente 6 caracteres (3 letras + 3 números).\nEjemplo: CM123")
            return
        
        # Verificar que los primeros 3 son letras
        if not codigo[:3].isalpha():
            messagebox.showerror("Error", "Los primeros 3 caracteres del código deben ser letras.\nEjemplo: CM123")
            return
        
        # Verificar que los últimos 3 son números
        if not codigo[3:].isdigit():
            messagebox.showerror("Error", "Los últimos 3 caracteres del código deben ser números.\nEjemplo: CM123")
            return
        
        # Validar número de vuelo
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        # Validar precio
        try:
            precio = float(texto_precio)
            if precio <= 0:
                messagebox.showerror("Error", "El precio debe ser mayor a 0.")
                return
        except:
            messagebox.showerror("Error", "El precio debe ser un número válido.")
            return
        
        # Asignar datos al vuelo (índice es num_vuelo - 1)
        indice = num_vuelo - 1
        vuelos[indice][0] = codigo      # Código (ya en mayúsculas)
        vuelos[indice][1] = origen      # Origen
        vuelos[indice][2] = destino     # Destino
        vuelos[indice][3] = precio      # Precio
        
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
        # Obtener valores
        texto_vuelo = entry_vuelo.get().strip()
        letra_fila = entry_fila.get().strip().upper()  # Convertir a mayúscula
        texto_columna = entry_columna.get().strip()
        
        # Validar que no estén vacíos
        if texto_vuelo == "" or letra_fila == "" or texto_columna == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        # Validar número de vuelo
        try:
            num_vuelo = int(texto_vuelo)
        except:
            messagebox.showerror("Error", "El número de vuelo debe ser un entero.")
            return
        
        if num_vuelo < 1 or num_vuelo > len(vuelos):
            messagebox.showerror("Error", f"El vuelo debe estar entre 1 y {len(vuelos)}.")
            return
        
        # Obtener el vuelo
        indice_vuelo = num_vuelo - 1
        vuelo = vuelos[indice_vuelo]
        
        # Verificar que el vuelo tenga datos asignados
        if vuelo[0] == "" or vuelo[1] == "" or vuelo[2] == "":
            messagebox.showerror("Error", "Este vuelo no tiene origen/destino asignado.\nUsa la opción 2 primero.")
            return
        
        # Validar que la letra sea solo una letra
        if len(letra_fila) != 1 or not letra_fila.isalpha():
            messagebox.showerror("Error", "La fila debe ser una sola letra (A, B, C...).")
            return
        
        # Convertir letra a índice de fila (A=0, B=1, C=2...)
        indice_fila = ord(letra_fila) - ord('A')
        
        # Validar número de columna
        try:
            num_columna = int(texto_columna)
        except:
            messagebox.showerror("Error", "La columna debe ser un número.")
            return
        
        if num_columna < 1:
            messagebox.showerror("Error", "La columna debe ser mayor o igual a 1.")
            return
        
        # Convertir a índice (columna 1 = índice 0)
        indice_columna = num_columna - 1
        
        # Obtener matriz de asientos
        matriz = vuelo[4]
        num_filas = len(matriz)
        num_columnas = len(matriz[0]) if num_filas > 0 else 0
        
        # Validar que el asiento existe
        if indice_fila < 0 or indice_fila >= num_filas:
            messagebox.showerror("Error", f"La fila {letra_fila} no existe.\nEste vuelo tiene filas de A hasta {chr(num_filas - 1 + ord('A'))}.")
            return
        
        if indice_columna < 0 or indice_columna >= num_columnas:
            messagebox.showerror("Error", f"La columna {num_columna} no existe.\nEste vuelo tiene columnas de 1 hasta {num_columnas}.")
            return
        
        # Verificar si el asiento está libre (0 = libre, 1 = ocupado)
        if matriz[indice_fila][indice_columna] == 1:
            messagebox.showerror("Error", f"El asiento {letra_fila}{num_columna} ya está ocupado.")
            return
        
        # Reservar el asiento
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
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton3.pack(pady=5)

boton4 = tk.Button(frame_botones, text="4. Reservar asiento", width=34,
                 command=reservar_asiento,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton4.pack(pady=5)

boton5 = tk.Button(frame_botones, text="5. Cancelar reserva", width=34,
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton5.pack(pady=5)

boton6 = tk.Button(frame_botones, text="6. Ver estadísticas de ocupación", width=34,
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton6.pack(pady=5)

boton7 = tk.Button(frame_botones, text="7. Ver estadísticas de recaudación", width=34,
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton7.pack(pady=5)

boton8 = tk.Button(frame_botones, text="8. Buscar vuelos por destino", width=34,
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton8.pack(pady=5)

boton9 = tk.Button(frame_botones, text="9. Ver vuelos disponibles", width=34,
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton9.pack(pady=5)

boton10 = tk.Button(frame_botones, text="10. Reservar varios asientos consecutivos", width=34,
                  command=lambda: None,
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton10.pack(pady=5)

boton11 = tk.Button(frame_botones, text="11. Simular venta masiva", width=34,
                  command=lambda: None,
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton11.pack(pady=5)

boton12 = tk.Button(frame_botones, text="12. Reiniciar vuelo", width=34,
                  command=lambda: None,
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
