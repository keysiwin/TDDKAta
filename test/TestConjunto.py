import unittest
from src.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
   def test_conjunto_vacio( self ):
      conjunto = Conjunto([])
      self.assertIsNone(conjunto.promedio())