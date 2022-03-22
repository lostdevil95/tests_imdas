from pages.base_page import BasePage
from pages.elements import WebElement, ManyWebElements

class UserMainPage(BasePage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'http://172.17.127.22:3001'
        super().__init__(web_driver, url)

                    # ELEMENTS ON PAGE #

    tasks = WebElement(css_selector="a[href='/tasks/']")
    catalogs = WebElement(css_selector="a[href='/catalogs/']")
    settings = WebElement(css_selector="a[href='/settings/']")
    all_status = ManyWebElements(xpath="i[@class='far fa-check-circle text-success']")
    update = WebElement(css_selector="a[href='?action=update-status']")
    dropdown = WebElement(css_selector="a[role='button']")
    logout = WebElement(xpath="//a[contains(text(),'Выход')]")

    logs = WebElement(xpath="//a[@href='/logs/']")
    check_logs = WebElement(xpath="//h1[contains(text(),'Журналы')]")