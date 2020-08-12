# Launching a Selenium-Controlled Browser
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')


# Launching Chrome With Selenium
from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'C:\python\vrequests\chromedriver.exe')


# Closing the browser
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')

browser.quit()


# Headless Browsing In Chrome or Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path=r'C:\python\vrequests\geckodriver.exe')

browser.quit()

# Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
browser = webdriver.Chrome(options=options, executable_path=r'C:\python\vrequests\chromedriver.exe')

browser.quit()


# Fetching Specific Pages
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://duckduckgo.com/')


# Finding Elements On The Page
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://duckduckgo.com/')
element = browser.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
print(element)


# Typing Into A Text Input
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://duckduckgo.com/')
element = browser.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
element.send_keys('How do you automate a web browser?')


# How To Press Enter Key
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://duckduckgo.com/')
element = browser.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
element.send_keys('How do you automate a web browser?')
element.send_keys(Keys.RETURN)


# Selenium Easy Practice Examples
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

input_element = browser.find_element_by_id('user-message')
input_element.send_keys('Check out this great message!')

show_message_button = browser.find_element_by_xpath('//*[@id="get-input"]/button')
show_message_button.click()


# Two Inputs And A Buton Click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

input_element_one = browser.find_element_by_id('sum1')
input_element_one.send_keys('10')

input_element_two = browser.find_element_by_id('sum2')
input_element_two.send_keys('7')

get_total_element = browser.find_element_by_xpath('//*[@id="gettotal"]/button')
get_total_element.click()

result_element = browser.find_element_by_id('displayvalue')
print(result_element.text)


# Drag And Drop With ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source_element = browser.find_element_by_xpath('//*[@id="box7"]')
destination_element = browser.find_element_by_xpath('//*[@id="box107"]')
actions = ActionChains(browser)
actions.drag_and_drop(source_element, destination_element).perform()


# Example Application: Stock Quote Checker
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://finance.yahoo.com')

ticker_to_lookup = True
while (ticker_to_lookup != "q"):
    ticker_to_lookup = input('What ticker to you want to look up? (q to quit) ')

    if ticker_to_lookup == 'q':
        browser.quit()
        break

    quote_lookup_text_input = browser.find_element_by_xpath(
        '//*[@id="Col2-0-SymbolLookup-Proxy"]/div/div/div/fieldset/input')
    quote_lookup_text_input.send_keys(ticker_to_lookup, Keys.RETURN)
    time.sleep(10)

    quote_span = browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div[3]/div[1]/div/span[1]')
    print(ticker_to_lookup + ' is currently ' + quote_span.text)
    browser.back()
    time.sleep(5)


# An Example Of Using A Wait Function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(executable_path=r'C:\python\vrequests\geckodriver.exe')
browser.get('https://www.google.com/earth/')
wait = WebDriverWait(browser, 10)
launchButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a')))
launchButton.click()



