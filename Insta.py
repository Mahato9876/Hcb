from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path="chromedriver.exe")
browser = webdriver.Chrome(service=service)
actions = ActionChains(browser)

browser.get("https://instagram.com")
time.sleep(4)
def login():
    username = browser.find_element(By.XPATH , "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[1]/div/label/input")
    username.send_keys('9142981933')
    time.sleep(4)
    password = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[2]/div/label/input')
    password.send_keys('Verified@533')
    password.submit()
    time.sleep(4)
# login()
def notifications():
    nn = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div")
    nn.click()
    nf = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    nf.click()
    time.sleep(4)
# notifications()
def meassage():
    icon = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a')
    icon.click()
    time.sleep(4)
    p1 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]')
    p1.click()
    # p1.send_keys(Keys.F11)
    time.sleep(4)
# meassage()

def fullscreen():
    body = browser.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.F11)

def backPage():
    body = browser.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ALT + Keys.ARROW_LEFT)

def clicking(xp):
    btn = browser.find_element(By.XPATH , xp)
    btn.click()
 
def submiting1(xp , txt ):
    btn = browser.find_element(By.XPATH , xp)
    btn.send_keys(txt)

def submiting2(xp , txt ):
    btn = browser.find_element(By.XPATH , xp)
    btn.send_keys(txt)
    btn.submit()

def gotohover(xp):
    element_to_hover_over = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, xp)) 
    )
    actions.move_to_element(element_to_hover_over).perform()

def enter_full_screen():
    browser.execute_script("document.documentElement.requestFullscreen();")

enter_full_screen()





#Main----------------------------------------------------
# fullscreen()
# enter_full_screen()

login()
# time.sleep(4)
notifications()
# time.sleep(4)

meassage()
time.sleep(4)

gotohover("/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[9]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div/div/div/div[4]")
#reply
time.sleep(4)

clicking('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[9]/div/div/div[2]/div[1]/div/div[3]/div[3]/div/div/div/div/div[2]/span/div/div/div')
#reply text
# submiting2('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[1]' , 'Heloo')






#--------------------------------------------------
while True:
    if input().strip().lower() == 'q':
        break

browser.quit()
