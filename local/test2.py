from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.google.co.jp/')
search = browser.find_element_by_name("q") #inputのname属性で指定
search.send_keys("Python") # send_keyでinput属性に入力
search.submit()
# browser.find_element_by_name("q").click() # 対象をクリック
