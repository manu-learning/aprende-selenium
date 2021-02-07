import unittest
from selenium.webdriver.common.keys import Keys

class Busqueda(object):
    # constructor
    def __init__(self, myDriver):
        self.driver = myDriver
        self.busqueda_box = self.driver.find_element_by_name('q')

    def buscar_texto(self, texto):
        # busqueda_box = self.driver.find_element_by_name('q')
        self.busqueda_box.send_keys(texto)
        self.busqueda_box.send_keys(Keys.ENTER)
        #self.verificar_busqueda(texto)

    def verificar_busqueda(self, texto):
        tc = unittest.TestCase('__init__')
        tc.assertEqual(self.busqueda_box.get_attribute('value'), texto)
