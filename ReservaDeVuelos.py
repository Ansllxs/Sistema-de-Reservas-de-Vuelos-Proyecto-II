import tkinter as tk
from tkinter import messagebox



# ---------- Datos (solo listas) y límites ----------
# Cada vuelo: [codigo, origen, destino, precio, matriz_asientos, cantidad_vendidos]
vuelos = []          # lista global de vuelos
MAX_FILAS = 50       # límite solicitado
MAX_COLUMNAS = 20    # límite solicitado

def crear_vuelo():
    """
    Ventana para crear un vuelo ingresando FILAS y COLUMNAS.
    Reglas:
      - enteros > 0
      - filas <= 50, columnas <= 20 (máximos permitidos)
    Guarda en: vuelos (lista global)
    """
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
            messagebox.showerror("Error", "Filas y columnas deben ser > 0.")
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
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton2.pack(pady=5)

boton3 = tk.Button(frame_botones, text="3. Ver estado de un vuelo", width=34,
                 command=lambda: None,
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton3.pack(pady=5)

boton4 = tk.Button(frame_botones, text="4. Reservar asiento", width=34,
                 command=lambda: None,
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
