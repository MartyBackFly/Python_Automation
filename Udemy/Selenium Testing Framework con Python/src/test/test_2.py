import unittest

class Test001(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 50
        self.Variable_B = 50

    def test_sum(self):
        resultado = self.Variable_A + self.Variable_B
        self.assertEqual(100, resultado, f"El valor no es 100, es {resultado}")


class Test002(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 'Mervin '
        self.Variable_B = 'Alberto'

    def test_concatenation(self):
        resultado = self.Variable_A + self.Variable_B
        self.assertEqual("Mervin Alberto", resultado, f"El resultado es diferente al esperado: {resultado}")


class Test003(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 'mamerto el 33 '
        self.Variable_B = 'ricardo'

    def test_concatenation(self):
        resultado = self.Variable_A + self.Variable_B
        self.assertEqual("mamerto el  ricardo", resultado, f"El resultado es diferente al esperado: {resultado}")


class Test004(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 'hola  '
        self.Variable_B = 'que tal'

    def test_concatenation(self):
        resultado = self.Variable_A + self.Variable_B
        self.assertEqual("hola  que tal", resultado, f"El resultado es diferente al esperado: {resultado}")

if __name__ == '__main__':
    unittest.main(exit=False)
