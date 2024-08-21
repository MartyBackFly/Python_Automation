from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az


def test_asserts():
    # Ejemplo 1: Verificar igualdad
    a = 2 + 3
    b = 5
    assert a == b, "a y b deberían ser iguales"

    # Ejemplo 2: Verificar desigualdad
    assert a != 4, "a no debería ser igual a 4"

    # Ejemplo 3: Verificar que un valor es verdadero
    assert b == 5, "b debería ser True"

    # Ejemplo 4: Verificar que un valor es falso
    assert not (b == 6), "b debería ser False"

    # Ejemplo 5: Verificar que un valor es None
    a = None
    assert a is None, "a debería ser None"

    # Ejemplo 6: Verificar que un valor no es None
    a = 10
    assert a is not None, "a no debería ser None"

    # Ejemplo 7: Verificar que un elemento está en una lista
    lista = [1, 2, 3, 4, 5]
    assert 3 in lista, "El elemento 3 debería estar en la lista"

    # Ejemplo 8: Verificar que un elemento no está en una lista
    assert 6 not in lista, "El elemento 6 no debería estar en la lista"

    # Ejemplo 9: Verificar que una cadena comienza con un prefijo
    cadena = "Hola, mundo"
    assert cadena.startswith("Hola"), "La cadena debería comenzar con 'Hola'"

    # Ejemplo 10: Verificar que una cadena termina con un sufijo
    assert cadena.endswith("mundo"), "La cadena debería terminar con 'mundo'"

    # Ejemplo 11: Verificar que un número está dentro de un rango
    numero = 7
    assert 0 <= numero <= 10, "El número debería estar entre 0 y 10"

    # Ejemplo 12: Verificar que una lista está vacía
    vacia = []
    assert not vacia, "La lista debería estar vacía"

    # Ejemplo 13: Verificar que una lista no está vacía
    no_vacia = [1]
    assert no_vacia, "La lista no debería estar vacía"

    # Ejemplo 14: Verificar que se lanza una excepción específica
    try:
        # Esto debería levantar una excepción ZeroDivisionError
        resultado = 1 / 0
    except ZeroDivisionError:
        pass  # La excepción esperada fue lanzada
    else:
        assert False, "Se esperaba un ZeroDivisionError"

# Ejecutar todas las pruebas
test_asserts()
print("Todas las pruebas pasaron correctamente.")
