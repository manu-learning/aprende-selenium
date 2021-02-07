from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 5)

web = "https://www.chessgames.com/perl/chessopening?eco=C60"
driver.get(web)

#self.selenium.switch_to.window(window_name=window_name)
#driver.execute_script('''window.open("http://bings.com","_blank");''')

# Removemos toda publicidad que impida nuestros clicks
driver.execute_script("""
var element = document.querySelector(".cc-banner"); if (element) element.parentNode.removeChild(element);
document.querySelectorAll("iframe").forEach(function(element){ element.remove(); })
document.querySelectorAll(".adsbygoogle").forEach(function(element){ element.remove(); })
document.querySelectorAll(".adsbyir").forEach(function(element){ element.remove(); })
""")

games_table = driver.find_element_by_xpath("/html/body/p[1]/table[1]/tbody/tr/td/table[2]")
first_game = games_table.find_elements_by_xpath("//a[starts-with(@href, '/perl/chessgame?gid=')]")[0]
first_game.click()
#game = games_table.find_element_by_xpath("//a[@href='/perl/chessgame?gid=1271912']")
