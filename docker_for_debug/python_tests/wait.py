# 必要なライブラリのインポート
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities

# ChromeのDriverを使ってseleniumHubにアクセスしdriver取得
driver = webdriver.Remote(command_executor='http://selenium_hub:4444/wd/hub',
                            desired_capabilities=DesiredCapabilities.CHROME.copy())

try:
    # google開く
    driver.get("https://www.google.co.jp/")
    
    # 待機処理
    # 検索ワードを入力する場所が表示されるまで最大30秒待機する
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "q")))
    
    # 検索ワードを入力する場所を探して「Selenium」と入力する
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('Selenium')

    # 検索を実行する（検索ボタンを押すのと同じ動作）
    search_box.submit() 

    # 検索結果からタイトルが「Selenium - Web Browser Automation」のリンクをクリックする。 
    driver.implicitly_wait(10)

    ## todo タイトルが無い時の処理を入れる
    driver.find_element_by_link_text("Selenium - Web Browser Automation").click()
    # 5秒待つ
    time.sleep(5)

finally:
    # Chromeブラウザを閉じる 
    # 閉じないと次のdriverを使った操作が出来ない
    driver.quit()