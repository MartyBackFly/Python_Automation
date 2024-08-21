from aafuncionimprimir import espacio as aa 
from aafuncionimprimir import rayita as zz 
from aafuncionimprimir import espacio_numero as az

import unittest


class test_001(unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        self.Variable_A = 50 
        self.Variable_B = 50
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertTrue(self.RESULTADO >= 100, "El valor no es 10")

    
    def test_002(self):
        self.assertEqual(sum([1,2,3]), 6, "Deberia ser 6")



    def test_003(self):
        self.Variable_A = 50 
        self.Variable_B = 40
        self.RESULTADO = self.Variable_A + self.Variable_B

        self.assertNotEqual(self.RESULTADO == 100, "El valor no es 10")


    def test_004(self):
        self.Variable_A = 50
        
        if self.Variable_A >= 10:
            self.RESULTADO = True
        
        else:
            self.RESULTADO = False
        
        self.assertTrue(self.RESULTADO, f"{self.Variable_A}La afirmacion no es True")

    
    
    def test_005(self):
        self.Variable_A = 50
        
        self.Variable_A = "ricardero"
        self.Variable_B = "esta ricardero presente en este string  ?"
        
        
        self.assertIn(self.Variable_A, self.Variable_B , f"{self.Variable_B} No contiene la palabra {self.Variable_A}")
 
 
    def test_006(self):
        self.Variable_A = 50
        
        self.Variable_A = "hola que tal queridisimo  "
        self.Variable_B = "hola que tal "
        
        
        self.assertIsNot(self.Variable_A, self.Variable_B , f"{self.Variable_B} es igual {self.Variable_A}")
    
    
    
    
    def tearDown(self):
        pass

aa()
class test_002(unittest.TestCase):

    def setUp(self):
        self.Variable_A = "Ricardo "
        self.Variable_B = "Alberto"
        
    def test_001(self):

        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self) -> None:
        self.assertEqual("Ricardo Alberto", self.RESULTADO, f"El resultado es diferente al esperado : {self.RESULTADO}")


if __name__ == "__main__":
    unittest.main()
