from selenium.webdriver.common.by import By
from .BasePage import BasePage
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class JqueryuiPage(BasePage):
    def __init__(self):
      BasePage.__init__(self)
      self.driver = super().driver()    
    
    # click on demos link 
    def click_on_demo(self):
      self.wait = WebDriverWait(self.driver, 10) 
      demo_xp = "//*[@id='menu-top']/li[1]/a"
      demo = self.wait.until(EC.element_to_be_clickable((By.XPATH, demo_xp)))
      demo.click()
   
    ################### start implement your logic here ##################
  



  

    ################### end implement your logic here ###############

    def cleanup(self):
      super().tearDown()

    def time_stamp(self):
      today = datetime.datetime.today()
      timestamp = today.strftime("%Y%m%d%H%M%S")
      return timestamp 

    def take_screenshot(self,title):
      super().screenshot(title)