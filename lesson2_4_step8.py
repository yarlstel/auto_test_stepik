from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    #sleep(1)

    #browser.find_element_by_class_name('btn').click()

    #sleep(2)

    #browser.switch_to.window(browser.window_handles[1])
    #sleep(1)
    
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    #browser.find_element_by_id('robotCheckbox').click()
    #browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_id('solve').click()
#    '''

finally:
    sleep(30)
    browser.quit() 