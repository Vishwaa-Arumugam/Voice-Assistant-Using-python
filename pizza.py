from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Jarvis import speak
from time import sleep

def pizza(self):
    driver = webdriver.Chrome(r"corresponding_path")

    driver.maximize_window()

    speak("Opening Dominos")

    driver.get('https://www.dominos.co.in/')
    sleep(2)

    speak("Getting Ready To Order")
    driver.find_element(By.LINK_TEXT,'ORDER ONLINE NOW').click()
    sleep(2)

    speak("finding your location")
    sleep(4)
    driver.find_element(By.XPATH,
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/label/input').click()
    sleep(2)

    location = "A B C"

    speak("Entering your location")
    driver.find_element(By.XPATH,
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(
        location)
    sleep(2)

    driver.find_element(By.XPATH,
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[3]/div[2]/span[1]').click()
    sleep(2)

    try:
        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[1]').click()
        sleep(2)

    except:

        speak("Your location could not be found")
        exit()

    speak("Logging in")

    phone_num = "your_num"

    driver.find_element(By.XPATH,
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div['
        '1]/div[2]/input').send_keys(
        phone_num)
    sleep(2)

    driver.find_element(By.XPATH,
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    sleep(2)

    speak("what is your OTP")
    sleep(5)

    otp_log = self.takeCommand()

    driver.find_element(By.XPATH,
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
        otp_log)
    sleep(2)

    driver.find_element(By.XPATH,
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
    sleep(2)

    speak("do you want me to order from your favourites")
    query_fav = self.takeCommand()
    speak("Ok sir, Adding your favourites to cart")

    if "yes" in query_fav:
        try:
            driver.find_element(By.XPATH,
                '//*[@id="mn-lft"]/div[2]/div/div[8]/div/div/div[2]/div[3]/div/button/span'
            ).click()
            sleep(2)
        except:
            speak("the entered OTP is incorrect")
            exit()

        speak("Favourites added to your cart")

        speak("do you want me to add extra cheese")
        ex_cheese = self.takeCommand()

        if "yes" in ex_cheese:
            speak("extra cheese added")
            driver.find_element(By.XPATH,
                '//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/button/span'
            ).click()
        elif "no" in ex_cheese:
            speak("Ok sir")
            driver.find_element(By.XPATH,
                '//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span'
            ).click()
        else:
            speak("I don't know that")
            driver.find_element(By.XPATH,
                '//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span'
            ).click()

        speak("Do you want me to add pepsi in the cart")
        add_beverage = self.takeCommand()
        if "yes" in add_beverage:
            speak("500ml pepsi added")
            driver.find_element(By.XPATH,
                '//*[@id="mn-lft"]/div[10]/div/div[1]/div/div/div[2]/div[2]/div/button/span').click()

        elif "no" in add_beverage:
            speak("ok sir")
            pass
        sleep(1)

        speak("checking out the order")
        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'
        ).click()
        sleep(2)

        total = driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[5]/span[2]/span')
        total_price = f'Total price is {total.text} rupees'
        speak(total_price)
        sleep(2)

        speak("placing your order")
        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button/span'
        ).click()
        sleep(2)

        speak("entering first name")

        first_name = ""

        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[1]/div/input').send_keys(
            first_name)
        sleep(2)

        speak("entering last name")

        last_name = ""

        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[2]/div/input').send_keys(
            last_name)
        sleep(2)

        speak("entering email address")

        email_address = ""

        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[2]/div/div/input').send_keys(
            email_address)
        sleep(2)

        speak("entering address")

        house_address = ""

        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[1]/div/input').send_keys(
            house_address)
        sleep(2)

        speak("entering house number")

        house_number = ""

        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[2]/div/input').send_keys(
            house_number)
        sleep(2)

        driver.find_element(By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()
        sleep(2)