# correr en la terminal con
# python -m unittest prueba-unitaria-1.py
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions

# importamos de busquedas.py
from Busqueda import *

class miPrueba(unittest.TestCase):
    # para iniciar
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.google.com.ar')
        self.busqueda = Busqueda(self.driver)

    def test_busqueda(self):
        self.busqueda.buscar_texto('escribiendo tururu')
        self.busqueda.verificar_busqueda('escribiendo tururuu')

     # para salir
    def tearDown(self):
        # time.sleep(3)
        self.driver.implicitly_wait(5)
        self.driver.quit()

    # def test_buscoTexto(self):
    #     busqueda_box = self.driver.find_element_by_name('q')
    #     busqueda_box.send_keys('escribiendo algo')
    #     busqueda_box.send_keys(Keys.ENTER)
    #     self.assertEqual(busqueda_box.get_attribute('value') , 'escribiendo algo')
