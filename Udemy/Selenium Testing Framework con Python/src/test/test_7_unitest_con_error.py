from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import unittest


class test_001(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.Variable_A = 50 
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertTrue(self.RESULTADO <= 99, "El valor no es 100")

    
    def test_2(self):
        self.assertEqual(sum([1,2,3]), 7, "Deberia ser 6")


    def test_003(self):
        self.Variable_A = 50 
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertNotEqual(self.RESULTADO , 100, "El valor no es igual ")



    def test_004(self):
        self.Variable_A = 9
        
        if self.Variable_A >= 10:
            self.RESULTADO = True
        
        else:
            self.RESULTADO = False
            self.assertTrue(self.RESULTADO, f"{self.Variable_A} La afirmacion no es ( >= 10 ) True")



    def test_005(self):
        self.Variable_A = 50
        
        self.Variable_A = "Ramon"
        self.Variable_B = "esta ricardero presente en este string  ?"
        
        
        self.assertIn(self.Variable_A, self.Variable_B , f"{self.Variable_B} --No contiene la palabra {self.Variable_A}")


    def tearDown(self):
        pass

aa()
class test_002(unittest.TestCase):

    def setUp(self):
        self.Variable_A = "Ricardo"
        self.Variable_B = "Alberto"
        
    def test_001(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self) -> None:
        self.assertEqual("Ricardo Alberto", self.RESULTADO, f"El resultado es diferente al esperado : {self.RESULTADO} diferente a Ricardo Alberto")


if __name__ == "__main__":
    unittest.main()
