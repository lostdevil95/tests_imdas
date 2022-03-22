from base_page import BasePage
from elements import WebElement, ManyWebElements

class MainPage(BasePage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'http://172.17.127.22:3001'
        super().__init__(web_driver, url)

    
