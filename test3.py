from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

def removeAds():
    driver.execute_script("""
    var element = document.querySelector(".cc-banner"); if (element) element.parentNode.removeChild(element);
    document.querySelectorAll("iframe").forEach(function(element){ element.remove(); })
    document.querySelectorAll(".adsbygoogle").forEach(function(element){ element.remove(); })
    document.querySelectorAll(".adsbyir").forEach(function(element){ element.remove(); })
    """)

profile = Options()
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir","/tmp/")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-chess-pgn,application/vnd.chess-pgn")

driver = webdriver.Firefox(options=profile)

driver.maximize_window()
wait = WebDriverWait(driver, 5)

web = "https://www.chessgames.com/perl/chessopening?eco=C60"
driver.get(web)

# Removemos toda publicidad que impida nuestros clicks
removeAds()

games_table = driver.find_element_by_xpath("/html/body/p[1]/table[1]")
list_games = games_table.find_elements_by_xpath("//a[starts-with(@href, '/perl/chessgame?gid=')]")
# colección tipo lista
list_links_games = []

for game in list_games:
    link_game = game.get_attribute('href')
    list_links_games.append(link_game)
    # print(game.get_attribute('href'))

window_main = driver.window_handles[0] # sin uso por ahora

for link_game in list_links_games:
    driver.execute_script('''window.open("","_blank");''')
    time.sleep(2)
    window_game = driver.window_handles[1]
    driver.switch_to.window(window_game)
    driver.get(link_game)

    removeAds()
    download_button = driver.find_element_by_xpath("//a[text()='download']")
    download_button.click()

    time.sleep(2)
    driver.close()
    driver.switch_to.window(window_main) # si no switcheas, luego rompe

    time.sleep(2)
