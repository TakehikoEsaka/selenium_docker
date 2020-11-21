from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

# seleniumのAPIサーバーはdockerで立てたサーバーに紐付いている
driver = webdriver.Remote(command_executor='http://selenium_hub:4444/wd/hub',
                            desired_capabilities=DesiredCapabilities.CHROME.copy())
try:
    driver.get('https://www.google.co.jp/')
    print('title:', driver.title)
finally:
    driver.quit()