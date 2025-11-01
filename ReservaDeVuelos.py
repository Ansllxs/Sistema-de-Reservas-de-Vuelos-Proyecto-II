import tkinter as tk

# --- Ventana principal---
ventana = tk.Tk()
ventana.title("Sistema de Reservas de Vuelos")
ventana.geometry("1000x650")
ventana.configure(bg="lavenderblush")  

# --- Paneles ---
panel_menu = tk.Frame(ventana, bd=1, relief="solid", bg="mistyrose") 
panel_menu.pack(side="left", fill="y")

panel_trabajo = tk.Frame(ventana, bd=1, relief="solid", bg="lavenderblush")
panel_trabajo.pack(side="right", fill="both", expand=True)

# --- titulo del sistema---
titulo = tk.Label(panel_trabajo,
                  text="Sistema de Reservas de Vuelos",
                  font=("Arial", 18, "bold"),
                  bg="lavenderblush", fg="dark slate gray")
titulo.pack(pady=12)

# --- area central apenas corre el sistema ---
area_texto = tk.StringVar()
area_texto.set("Bienvenido/a ✨\n\nElige una opción del menú de la izquierda.")
area_label = tk.Label(panel_trabajo,
                      textvariable=area_texto,
                      font=("Arial", 14),
                      justify="left",
                      anchor="nw",
                      bg="lavenderblush", fg="dark slate gray")
area_label.pack(fill="both", expand=True, padx=20, pady=20)


# --- BOTONES ---
boton1 = tk.Button(panel_menu, text="1. Crear nuevo vuelo", width=34,
                 command=lambda: area_texto.set("1) Crear nuevo vuelo"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton1.pack(padx=10, pady=5)

boton2 = tk.Button(panel_menu, text="2. Asignar origen/destino y precio a vuelo", width=34,
                 command=lambda: area_texto.set("2) Asignar origen/destino y precio a vuelo"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton2.pack(padx=10, pady=5)

boton3 = tk.Button(panel_menu, text="3. Ver estado de un vuelo", width=34,
                 command=lambda: area_texto.set("3) Ver estado de un vuelo"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton3.pack(padx=10, pady=5)

boton4 = tk.Button(panel_menu, text="4. Reservar asiento", width=34,
                 command=lambda: area_texto.set("4) Reservar asiento"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton4.pack(padx=10, pady=5)

boton5 = tk.Button(panel_menu, text="5. Cancelar reserva", width=34,
                 command=lambda: area_texto.set("5) Cancelar reserva"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton5.pack(padx=10, pady=5)

boton6 = tk.Button(panel_menu, text="6. Ver estadísticas de ocupación", width=34,
                 command=lambda: area_texto.set("6) Ver estadísticas de ocupación"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton6.pack(padx=10, pady=5)

boton7 = tk.Button(panel_menu, text="7. Ver estadísticas de recaudación", width=34,
                 command=lambda: area_texto.set("7) Ver estadísticas de recaudación"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton7.pack(padx=10, pady=5)

boton8 = tk.Button(panel_menu, text="8. Buscar vuelos por destino", width=34,
                 command=lambda: area_texto.set("8) Buscar vuelos por destino"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton8.pack(padx=10, pady=5)

boton9 = tk.Button(panel_menu, text="9. Ver vuelos disponibles", width=34,
                 command=lambda: area_texto.set("9) Ver vuelos disponibles"),
                 bg="pink", activebackground="hotpink",
                 fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton9.pack(padx=10, pady=5)

boton10 = tk.Button(panel_menu, text="10. Reservar varios asientos consecutivos", width=34,
                  command=lambda: area_texto.set("10) Reservar varios asientos consecutivos"),
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton10.pack(padx=10, pady=5)

boton11 = tk.Button(panel_menu, text="11. Simular venta masiva", width=34,
                  command=lambda: area_texto.set("11) Simular venta masiva"),
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton11.pack(padx=10, pady=5)

boton12 = tk.Button(panel_menu, text="12. Reiniciar vuelo", width=34,
                  command=lambda: area_texto.set("12) Reiniciar vuelo"),
                  bg="pink", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton12.pack(padx=10, pady=5)

boton13 = tk.Button(panel_menu, text="13. Salir", width=34,
                  command=ventana.destroy,
                  bg="white", activebackground="hotpink",
                  fg="dark slate gray", activeforeground="dark slate gray", bd=0)
boton13.pack(padx=10, pady=12)

# --- Iniciar app ---
ventana.mainloop()
