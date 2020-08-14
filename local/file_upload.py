from selenium import webdriver
browser = webdriver.Firefox()
browser.implicitly_wait(10) # 要素がみつかるまで待機する.
browser.get('http://demo.guru99.com/test/upload/') # アップロード用のデモサイト
search = browser.find_element_by_id("uploadfile_0") # inputのidで指定
search.send_keys("/home/chopprin/Dropbox/tips/Docker/392bd01be6aff9fc1dd4.pdf") # send_keyでinput属性に入
browser.find_element_by_id("terms").click()
browser.find_element_by_name("send").click()
# search.submit()
# browser.find_element_by_name("q").click() # 対象をクリック
