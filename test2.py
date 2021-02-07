from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

# Mas extensiones:
# https://www.freeformatter.com/mime-types-list.html

# con FirefoxProfile() no funcionaba la opcion neverAsk, a menos que usara alwaysAsk.force "que no me parecia prudente"
#profile = FirefoxProfile()
#profile.set_preference("browser.helperApps.alwaysAsk.force", False);
#profile.set_preference("browser.download.panel.shown", False)

profile = Options()
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir","/tmp/")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-chess-pgn,application/vnd.chess-pgn")

driver = webdriver.Firefox(options=profile)
#driver = webdriver.Firefox(firefox_profile=profile)
#driver = webdriver.Firefox()

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

driver.execute_script("""
var element = document.querySelector(".cc-banner"); if (element) element.parentNode.removeChild(element);
document.querySelectorAll("iframe").forEach(function(element){ element.remove(); })
document.querySelectorAll(".adsbygoogle").forEach(function(element){ element.remove(); })
document.querySelectorAll(".adsbyir").forEach(function(element){ element.remove(); })
""")
download_button = driver.find_element_by_xpath("//a[text()='download']")
download_button.click()
# /html/body/center[2]/table[1]
# $x("//a[text()='download']/@href")
#game = games_table.find_element_by_xpath("//a[@href='/perl/chessgame?gid=1271912']")
