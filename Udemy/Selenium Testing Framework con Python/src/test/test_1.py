import unittest


class test_001(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 50
        self.Variable_B = 50

    def test_001(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self):
        self.assertTrue(self.RESULTADO == 100, f"El valor no es 10, es {self.RESULTADO}")


class test_002(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 'Mervin '
        self.Variable_B = 'Alberto'

    def test_002(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self):
        self.assertEqual("Mervin Alberto", self.RESULTADO, f"El resultado es diferente al esperado: {self.RESULTADO}")



class Test003(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 'mamerto '
        self.Variable_B = 'ricardo'

    def test_concatenation(self):
        resultado = self.Variable_A + self.Variable_B
        self.assertEqual("mamerto el ricardo", resultado, f"El resultado es diferente al esperado: {resultado}")

    def tearDown(self):
        pass



class test_004(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 'hola '
        self.Variable_B = 'que tal'

    def test_004(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self):
        self.assertEqual("hola que tal", self.RESULTADO, f"El resultado es diferente al esperado: {self.RESULTADO}")        


if __name__ == "__main__":
    unittest.main(exit=False)