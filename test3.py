import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

class DescargaAutomatica(unittest.Testcase):
    def setUp(self):
        profile = Options()
        profile.set_preference("browser.download.folderList",2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir","/tmp/")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-chess-pgn,application/vnd.chess-pgn")

        driver = webdriver.Firefox(options=profile)
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()

    def removeAds():
        driver.execute_script("""
        var element = document.querySelector(".cc-banner"); if (element) element.parentNode.removeChild(element);
        document.querySelectorAll("iframe").forEach(function(element){ element.remove(); })
        document.querySelectorAll(".adsbygoogle").forEach(function(element){ element.remove(); })
        document.querySelectorAll(".adsbyir").forEach(function(element){ element.remove(); })
        """)


    def tearDown(self):
        self.driver.implicity_wait(5)
        self.driver.quit()

    def test_descargar(self):
        window_main = self.driver.window_handles[0] # sin uso por ahora
        web = "https://www.chessgames.com/perl/chessopening?eco=C60"
        self.driver.get(web)
        #removeAds()

        games_table = self.driver.find_element_by_xpath("/html/body/p[1]/table[1]")
        list_games = games_table.find_elements_by_xpath("//a[starts-with(@href, '/perl/chessgame?gid=')]")
        list_links_games = []

        for game in list_games:
            link_game = game.get_attribute('href')
            list_links_games.append(link_game)


            for link_game in list_links_games:
                self.driver.execute_script('''window.open("","_blank");''')
                time.sleep(2)
                window_game = driver.window_handles[1]
                self.driver.switch_to.window(window_game)
                self.driver.get(link_game)

                download_button = driver.find_element_by_xpath("//a[text()='download']")
                removeAds()
                download_button.click()

                time.sleep(2)
                self.driver.close()
                self.driver.switch_to.window(window_main) # si no switcheas, luego rompe
                time.sleep(2)
