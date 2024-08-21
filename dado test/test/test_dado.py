import unittest
from unittest.mock import patch
import sys
import os



# Añadir el directorio src al path de búsqueda de módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import dado  # Ahora deberías poder importar dado correctamente

class TestDadoApp(unittest.TestCase):
    def setUp(self):
        self.ventana, self.boton, self.etiqueta_resultado = dado.crear_ventana()

    def tearDown(self):
        self.ventana.destroy()
    

   


    @patch('random.randint', return_value=3)
    def test_boton_presionado(self, mock_randint):
        self.boton.invoke()  # Simula un clic en el botón
        self.assertEqual(self.etiqueta_resultado.cget("text"), "Salio: 3")

if __name__ == '__main__':
    unittest.main()



""" 
Explicación
Código Principal Modificado:

Envuelve la creación de la ventana en una función crear_ventana que retorna los widgets principales 
para que puedan ser manipulados en las pruebas.


Script de Prueba:

Utiliza unittest para estructurar las pruebas.
Usa setUp para crear la ventana antes de cada prueba y tearDown para destruirla después de cada prueba.
Emplea unittest.mock.patch para controlar el resultado de random.randint y así poder predecir el resultado esperado.
Simula un clic en el botón usando self.boton.invoke() y verifica que el texto de etiqueta_resultado es el esperado.
Con esta estructura, puedes ejecutar test_dado.py y verificar que tu aplicación Tkinter se comporta correctamente bajo 
las condiciones de prueba controladas.

"""