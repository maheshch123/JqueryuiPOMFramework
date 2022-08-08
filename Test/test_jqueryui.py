from page.JqueryuiPage import JqueryuiPage
import sys

page_Jqueryui = JqueryuiPage()

def test_jqueryui():
    title = sys._getframe().f_code.co_name
    try:

        # used to click on demos link
        page_Jqueryui.click_on_demo()
    
        ################### start implement your logic here ##################







        ################### end implement your logic here ###############

        page_Jqueryui.take_screenshot("debug-Jqueryui-") # take screenshot
        # page_Jqueryui.cleanup() # close browser
    except:
        page_Jqueryui.take_screenshot("FAIL- "+title)   # take screenshot if test fails
        # page_Jqueryui.cleanup() # close browser
        assert False, "FAIL"
