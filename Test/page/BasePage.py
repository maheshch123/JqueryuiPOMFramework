from selenium import webdriver
import datetime


WEBURL = "https://jqueryui.com/"

class BasePage:
    def setUp(self):

        chromedriver_path = 'C:\\Users\\hp\\drivers\\chromedriver.exe' 
        self.driver = webdriver.Chrome(chromedriver_path)
        self.driver.get(WEBURL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    

    def driver(self):
       return self.driver

    def tearDown(self):
        if (self.driver != None):
          print("Cleanup of test environment")
          self.driver.close()
          self.driver.quit()
    
    def screenshot(self,title):
        today = datetime.datetime.today()
        timestamp = today.strftime("%Y%m%d%H%M%S")
        self.driver.save_screenshot(f'{timestamp}-{title}.png')
    

    def __init__(self):
        self.setUp()

