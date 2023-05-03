from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Jarvis import speak
import pyautogui


def amazon(self):
    driver = webdriver.Chrome(r"C:\Users\Vishwaa Arumugam\Desktop\chromedriver.exe")

    driver.maximize_window()
    sleep(2)

    speak("opening amazon")

    driver.get("https://www.amazon.in/")
    sleep(2)

    speak("logging in")

    driver.find_element(By.XPATH,'//*[@id="nav-link-accountList-nav-line-1"]').click()
    sleep(2)

    mob_num = "----------"

    speak("entering your mobile number")
    driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys(mob_num)
    sleep(2)

    driver.find_element(By.XPATH,'//*[@id="continue"]').click()
    sleep(2)

    pass_word = "pass"

    speak("entering your password")

    driver.find_element(By.XPATH,'//*[@id="ap_password"]').send_keys(pass_word)
    sleep(2)

    driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
    sleep(2)

    speak("ordering a mobile phone")

    driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]/i').click()
    sleep(2)

    driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[15]/a').click()
    sleep(2)

    driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[8]/li[3]/a').click()
    sleep(2)

    # Choosing mobile's brand

    driver.execute_script("window.scrollTo(0,300)")

    speak("which brand do you want me to order?")
    brand = self.takeCommand()
    speak("ok sir")

    if "oneplus" in brand:
        try:
            driver.find_element(By.XPATH,
                '//*[@id="s-refinements"]/div[5]/ul/li[1]/span/a/div/label/i').click()
            sleep(2)
        except:
            driver.find_element(By.XPATH,
                '//*[@id="s-refinements"]/div[5]/ul/li[1]/span/a/div/label/i').click()
            sleep(2)

    # Choosing brand's model

    speak("which model do you want me to order?")
    model = self.takeCommand()
    speak("ok sir")

    if "oneplus" in model:
        try:
            driver.find_element(By.XPATH,
                '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div[1]/span/a/div/img').click()
            sleep(2)
        except:
            driver.find_element(By.XPATH,
                '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div[1]/span/a/div/img').click()
            sleep(2)

    driver.switch_to_window(driver.window_handles[1])

    speak("Do you want to buy this phone or i just add this to your cart sir?")
    buy = self.takeCommand()
    speak("ok sir")

    if "order now" in buy:
        driver.find_element(By.XPATH,
            '//*[@id="buy-now-button"]').click()
        sleep(2)
    else:
        driver.find_element(By.XPATH,
            '//*[@id="buy-now-button"]').click()
        sleep(7)

    speak("Which address do you want me to select or i create a new one")

    address = self.takeCommand()
    speak("ok sir")
    if "select first address" in address:
        try:
            driver.find_element(By.XPATH,'//*[@id="address-book-entry-0"]/div[2]/span/a').click()
            sleep(2)
        except:
            driver.find_element(By.XPATH,'//*[@id="address-book-entry-0"]/div[2]/span/a').click()

    else:
        driver.find_element(By.XPATH,'//*[@id="address-book-entry-0"]/div[2]/span/a').click()
        sleep(2)

    page = driver.find_element_by_tag_name("html")
    page.send_keys(Keys.END)
    sleep(2)

    pyautogui.click(x=272, y=633)
    sleep(2)

    speak("confirm order")
    pyautogui.click(x=1469, y=783)
    sleep(2)

    total_price = driver.find_element(By.XPATH,
        '//*[@id="subtotals-marketplace-table"]/tbody/tr[6]/td[2]')
    total_price = f'Total price is {total_price.text}'
    speak(total_price)
    sleep(2)

    speak("ok sir, placing your order")
    driver.find_element('//*[@id="placeYourOrder"]/span/input').click()
    sleep(2)