import tkinter as tk
from tkinter import messagebox

# ----------------------------
# FUNCION PRINCIPAL
# ----------------------------
def determinar_pavimento():
    try:
        # Se leen los datos que el usuario escribió en la interfaz
        esal = float(entry_esal.get())  # Tráfico acumulado
        cbr = float(entry_cbr.get())    # Resistencia del suelo
        clima = clima_var.get()         # Clima seleccionado

        # ----------------------------
        # EXPLICACIÓN DE LAS VARIABLES
        # ----------------------------
        # ESAL = "Equivalent Single Axle Load" (Ejes equivalentes de carga)
        # Representa cuánto tráfico pesado soportará el pavimento.
        # Si el ESAL es alto, hay mucho tráfico → se recomienda pavimento rígido.

        # CBR = "California Bearing Ratio"
        # Mide la capacidad del suelo para resistir carga.
        # Cuanto más alto el CBR (%), más fuerte es el suelo.
        # Si el CBR es bajo, el terreno es débil → se recomienda pavimento rígido.

        # ----------------------------
        # CONDICIONES DE DECISIÓN
        # ----------------------------
        if esal > 1_000_000 or cbr < 5:
            tipo = "RÍGIDO"
            razon = (
                "Se recomienda pavimento RÍGIDO porque el tráfico (ESAL) es alto "
                "o el suelo tiene baja resistencia (CBR bajo)."
            )
        else:
            tipo = "FLEXIBLE"
            razon = (
                "Se recomienda pavimento FLEXIBLE porque el tráfico (ESAL) es moderado "
                "y el suelo tiene buena resistencia (CBR adecuado)."
            )

        # Ajuste adicional según el clima
        if clima in ["Húmedo", "Muy húmedo"]:
            razon += "\nEl clima húmedo acelera el deterioro, por lo que se deben usar materiales de buena calidad."
        elif clima == "Frío":
            razon += "\nEl clima frío puede causar grietas, se recomienda diseño que soporte cambios térmicos."

        # Mostrar resultado en pantalla
        messagebox.showinfo("Resultado", f"Tipo de pavimento recomendado: {tipo}\n\n{razon}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números válidos en ESAL y CBR.")

# ----------------------------
# INTERFAZ GRÁFICA
# ----------------------------
ventana = tk.Tk()
ventana.title("Determinador de Tipo de Pavimento")
ventana.geometry("450x380")
ventana.resizable(False, False)

# Título
tk.Label(ventana, text="DETERMINADOR DE TIPO DE PAVIMENTO", font=("Arial", 14, "bold")).pack(pady=10)

# Entrada de ESAL
tk.Label(ventana, text="Tráfico acumulado (ESAL):").pack()
entry_esal = tk.Entry(ventana)
entry_esal.pack(pady=5)

# Entrada de CBR
tk.Label(ventana, text="CBR del suelo (%):").pack()
entry_cbr = tk.Entry(ventana)
entry_cbr.pack(pady=5)

# Selección de clima
tk.Label(ventana, text="Condición climática:").pack()
clima_var = tk.StringVar(value="Seco")
opciones_clima = ["Seco", "Templado", "Húmedo", "Muy húmedo", "Frío"]
tk.OptionMenu(ventana, clima_var, *opciones_clima).pack(pady=5)

# Botón para calcular
tk.Button(
    ventana,
    text="Determinar tipo de pavimento",
    command=determinar_pavimento,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

# Iniciar la interfaz
ventana.mainloop()
