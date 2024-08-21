import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        # Inicialización común para todas las pruebas
        pass

    def test_001(self):
        Variable_A = 50
        Variable_B = 50
        
        resultado = Variable_A + Variable_B
        self.assertEqual(resultado, 100, f"El resultado del test_001 no es 100, es {resultado}")

    def test_002(self):
        Variable_A = 'Mervin '
        Variable_B = 'Alberto'
        resultado = Variable_A + Variable_B
        self.assertEqual(resultado, "Mervin Alberto", f"El resultado del test_002 es diferente al esperado: {resultado}")

    def test_003(self):
        Variable_A = 'mamerto '
        Variable_B = 'ricardo'
        resultado = Variable_A + 'el ' + Variable_B
        self.assertEqual(resultado, "mamerto el ricardo", f"El resultado del test_003 es diferente al esperado: {resultado}")

    def test_004(self):
        Variable_A = 'hola '
        Variable_B = 'que tal'
        resultado = Variable_A + Variable_B
        self.assertEqual(resultado, "hola que tal", f"El resultado del test_004 es diferente al esperado: {resultado}")

    def tearDown(self):
        # Limpieza final, si es necesaria
        pass

if __name__ == "__main__":
    unittest.main(exit=False)
