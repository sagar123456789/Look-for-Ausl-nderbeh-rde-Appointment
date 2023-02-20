# Appointment data looker
# Author: Sagar GR

from asyncio.windows_events import NULL
import undetected_chromedriver as uc
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


opts = uc.ChromeOptions()
opts.add_argument("--window-size=1020,900")  

driver = uc.Chrome(options=opts, use_subprocess=True,version_main=107)

driver.get('https://otv.verwalt-berlin.de/ams/TerminBuchen')

driver.find_element(By.XPATH,'//*[@id="mainForm"]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="xi-div-1"]/div[4]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="applicationForm:managedForm:proceed"]').click()
# time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="xi-sel-400"]/option[64]').click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="xi-sel-400"]')))

dropdown_trigger =Select(driver.find_element(By.XPATH,'//*[@id="xi-sel-400"]')) 
driver.implicitly_wait(10)
# dropdown_trigger.select_by_value("436")
dropdown_trigger.select_by_visible_text("Indien")

dropdown_trigger =Select(driver.find_element(By.XPATH,'//*[@id="xi-sel-422"]')) 
driver.implicitly_wait(10)
# dropdown_trigger.select_by_value("436")
dropdown_trigger.select_by_visible_text("eine Person")

dropdown_trigger =Select(driver.find_element(By.XPATH,'//*[@id="xi-sel-427"]')) 
driver.implicitly_wait(10)
# dropdown_trigger.select_by_value("436")
dropdown_trigger.select_by_visible_text("nein")

driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="xi-div-30"]/div[2]/label').click()

driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="inner-436-0-2"]/div/div[1]/label').click()

time.sleep(5)

def WakeUp():
    opts = uc.ChromeOptions()
    opts.add_argument("--window-size=1020,900")  
    driver2 = uc.Chrome(options=opts, use_subprocess=True)
    driver2.get('https://www.youtube.com/watch?v=o4rtq27p3OE&ab_channel=HappyMusic')
    time.sleep(3)

    driver2.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
    
    video = driver2.find_element(By.ID,'movie_player')
    time.sleep(2)


driver.find_element(By.XPATH,'//*[@id="SERVICEWAHL_DE436-0-2-3-305244"]').click()
time.sleep(5)
abc=0
def refresh():
    driver.find_element(By.XPATH,'//*[@id="applicationForm:managedForm:proceed"]').click()
    time.sleep(7)
    try: 
        abc=driver.find_element(By.XPATH,'//*[@id="messagesBox"]')
        refresh()
    except NoSuchElementException as ex:
        # WakeUp()
        print(ex)
    finally:
        time.sleep(1000)    
    
    # try: 
    #     dateselector=driver.find_element(By.CLASS_NAME,'ui-state-highlight').click()
    # except NoSuchElementException as ex:
    #     print(ex)

    try: 
        abc=driver.find_element(By.XPATH,'//*[@id="xi-div-2"]/div')
        # WakeUp()
    except NoSuchElementException as ex:
        print(ex)
    finally:
        time.sleep(1000)    
refresh()

time.sleep(1000)
driver.close()


# WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]')))

# button = driver.find_element(By.XPATH,'//*[@id="applicationForm:managedForm:proceed"]')
# driver.execute_script("arguments[0].click();", button)
# driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[4]/div[2]/form/div[5]/button').click()

# driver.implicitly_wait(20)
# dropdown_trigger = driver.find_element(By.XPATH,'//*[@id="xi-sel-400"]')
# driver.execute_script("arguments[0].click();", dropdown_trigger)

# dropdown_option = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="xi-sel-400"]/option[64]')))
# dropdown_option.click()

# email_field = driver.find_element(By.ID, "identifierId")
# email_field.clear()

