import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

usr = "joe@demo.com" 
pwd = "carbonCopee"

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
	driver = webdriver.Chrome("C:\Users\QingW\PycharmProjects\FirstSeleium\Driver\chromedriver.exe")
	driver.get("https://model.arxspan.com/login.asp") 

        
    # Test title1
    def testTitle1(self):
	assert "Arxspan" in driver.title 

        
    # Test successful login
    def testSuccessfulLogin(self):
	elem = driver.find_element_by_id("login-email") 
	elem.send_keys(usr) 
	elem = driver.find_element_by_id("login-pass") 
	elem.send_keys(pwd) 
	elem.send_keys(Keys.RETURN)

	select = Select(driver.find_element_by_tag_name("select")) 
	select.select_by_visible_text("Demo") 
	elem = driver.find_element_by_id("login-submit")
	elem.send_keys(Keys.ENTER)
	
	assert "" # after success login, should assert either page or success message

    # Test unsuccessful login - wrong password
    def testSuccessfulLoginWrongPassword(self):
	#TODO


    # Test unsuccessful login - wrong username
    def testSuccessfulLoginWrongUsername(self):
	#TODO
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
