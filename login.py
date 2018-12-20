from selenium import webdriver from selenium.webdriver.common.keys import Keys from selenium.webdriver.support.ui import Select

usr = "joe@demo.com" 
pwd = "carbonCopee"

driver = webdriver.Chrome("C:\Users\QingW\PycharmProjects\FirstSeleium\Driver\chromedriver.exe")

driver.get("https://model.arxspan.com/login.asp") 

assert "Arxspan" in driver.title 
elem = driver.find_element_by_id("login-email") 
elem.send_keys(usr) 
elem = driver.find_element_by_id("login-pass") 
elem.send_keys(pwd) 

elem.send_keys(Keys.RETURN)

select = Select(driver.find_element_by_tag_name("select")) 
select.select_by_visible_text("Demo") 
elem = driver.find_element_by_id("login-submit")
elem.send_keys(Keys.ENTER)

driver.close()
