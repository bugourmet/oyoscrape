from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumwire import webdriver 
#from selenium.webdriver import ActionChains
import cfg as config

option = webdriver.ChromeOptions()
option.binary_location = config.browser_path
option.add_argument("--incognito") 
driver = webdriver.Chrome(executable_path=config.driver_path, chrome_options=option)


def main():
    driver.get("https://novaplus.dnevnik.hr/")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.nav-start.block-button.arrow-button"))).click()
    element = driver.find_element_by_css_selector('[data-event="login"]')
    driver.execute_script("arguments[0].click();", element)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input.mb-20.g100"))).send_keys(config.email_address)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input.mb-20.g100.field-pass"))).send_keys(config.password)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.dialog-button.g100.icon-lock-open-alt"))).click()
    link_serije = input("Unesi link serije: ")
    driver.get(link_serije)
    element2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.fp-ui")))
    driver.execute_script("arguments[0].click();", element2)
    sleep(3) #cekamo da se obave ostali requestovi(playlist get request),povecaj ako ti je internet 💩
    for requests in driver.requests:
        if 'playlist.m3u8' in requests.path:
            print("Playlist download link:")
            print(requests.url)
            driver.get(str(requests.url))
    sleep(10)


main()