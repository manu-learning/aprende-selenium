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

time.sleep(5)

# 

for i in range(3):
    driver.execute_script("""
    var element = document.querySelector(".cc-window");
    if (element) element.parentNode.removeChild(element);
    """)

    if i == 0:
        games_table = driver.find_element_by_xpath("/html/body/p[1]/table[1]")
    else:
        games_table = driver.find_element_by_xpath("/html/body/p[2]/table[1]")

    list_games = games_table.find_elements_by_xpath("//a[starts-with(@href, '/perl/chessgame?gid=')]")

    print("PAGINA %d" %i)

    for game in list_games:
        print(game.text)
        #time.sleep(1)

    button_next_game = games_table.find_elements_by_xpath("//img[contains(@src, '/chessimages/next.gif')]")[1]
    wait.until(EC.element_to_be_clickable, button_next_game)

    button_next_game.click()
    time.sleep(5)

#driver.close()


