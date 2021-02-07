from selenium import webdriver
# para usar el sleep
import time
# para usar teclas como enter
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://google.com')
time.sleep(2)

busqueda_box = driver.find_element_by_name('q')
# submit_button = driver.find_element_by_name('btnK') # por ahora no me sirve, no puedo clickearlo

busqueda_box.send_keys('mafalda san telmo')
busqueda_box.send_keys(Keys.ENTER)
# submit_button.click() # esto no anda con el el buscador de google
# driver.quit()

