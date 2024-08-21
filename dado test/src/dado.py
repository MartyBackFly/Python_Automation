import tkinter as tk
import random

def crear_ventana():
    def boton_presionado():
        resultado = random.randint(1, 6)
        etiqueta_resultado.config(text=f"Salio: {resultado}")

    ventana = tk.Tk()
    ventana.config(width=500, height=300)
    ventana.title("Tirar el dado")

    boton = tk.Button(ventana, text="Arrojar dado", command=boton_presionado)
    boton.place(x=20, y=120, width=200, height=25)

    etiqueta = tk.Label(ventana, text="Presiona el botón para arrojar el dado", font=("Arial", 18))
    etiqueta.place(x=20, y=90, anchor="w")

    etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 18))
    etiqueta_resultado.place(x=20, y=160)

    return ventana, boton, etiqueta_resultado

if __name__ == "__main__":
    ventana, boton, etiqueta_resultado = crear_ventana()
    ventana.mainloop()
