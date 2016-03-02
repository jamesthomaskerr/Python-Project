import unittest
from test4 import *
from p_rates import *


class TestMyMethods(unittest.TestCase):

    #Testing weather a string containing numbers can use the .upper function
  def test_upper(self):
      self.assertEqual('foo2'.upper(), 'FOO2')

    #Testing route to see if the distance is equal, if the route is reversed but has the same home.
  def test_distance(self):
      dis=TAirportatlas()
      self.assertEqual(dis.distanceBetweenAirports("DUB","lhr","jfk","aal","dub"),
                       dis.distanceBetweenAirports("dub","aal","jfk","lhr","dub"))

    #Test that cost of €1 to € in Dub is = 1
  def test_EuroRate(self):
      euro=Rates()
      self.assertEqual(euro.fromeuro(1,"DUB"),1)

  def test_isupper(self):
      self.assertTrue('BAE146'.isupper())
      self.assertFalse('a320'.isupper())


if __name__ == '__main__':
    unittest.main()