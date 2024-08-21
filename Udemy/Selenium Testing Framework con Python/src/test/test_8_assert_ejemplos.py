from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


def test_asserts():
    # Ejemplo 1: Verificar igualdad
    resultado = 2 + 3
    assert resultado == 5, "La suma debería ser 5"

    # Ejemplo 2: Verificar que una lista contenga un elemento
    lista = [1, 2, 3, 4, 5]
    assert 3 in lista, "El elemento 3 debería estar en la lista"

    # Ejemplo 3: Verificar que una cadena comienza con un prefijo específico
    cadena = "Hola, mundo"
    assert cadena.startswith("Hola"), "La cadena debería comenzar con 'Hola'"

    # Ejemplo 4: Verificar que una excepción se lanza
    try:
        1 / 0
    except ZeroDivisionError:
        pass  # La excepción esperada fue lanzada
    else:
        assert False, "Se esperaba un ZeroDivisionError"

    # Ejemplo 5: Verificar que dos listas sean iguales
    lista1 = [1, 2, 3]
    lista2 = [1, 2, 3]
    assert lista1 == lista2, "Las listas deberían ser iguales"

# Ejecutar todas las pruebas
test_asserts()
print("Todas las pruebas pasaron correctamente.")
