from .base_page import BasePage
from pages.elements import WebElement

class AuthPage(BasePage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'http://172.17.127.22:3001/'
        super().__init__(web_driver, url)

    imdas = WebElement(css_selector='.navbar-brand')
    login = WebElement(id='id_login')
    domain = WebElement(id='id_domain')
    password = WebElement(id='id_password')
    enter = WebElement(tag_name='button')
