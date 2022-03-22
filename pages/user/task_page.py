from pages.base_page import BasePage
from pages.elements import WebElement, ManyWebElements

class UserTaskPage(BasePage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'http://172.17.127.22:3001/tasks/'
        super().__init__(web_driver, url)

                                          #TASKS#

    #.... System-wide software....#
    create_vm = WebElement(css_selector="a[href='/tasks/common/virtual-machines/create/']")
    delete_vm = WebElement(xpath="//a[contains(text(),'Удаление виртуальной машины')]")
    update_server = WebElement(css_selector="a[href='/tasks/common/virtual-machines/update/']")
    create_file_source = WebElement(css_selector="a[href='/tasks/common/virtual-machines/create-file-resource/']")
    create_group_AD = WebElement(xpath="//a[contains(text(),'Создание группы Active Directory')]")
    create_service_acc_AD = WebElement(xpath="//a[contains(text(),'Создание сервисной учетной записи')]")
    create_email_AD = WebElement(xpath="//a[contains(text(),'Создание почтового ящика')]")
    # ....Basic network services....#
    edit_DDI = WebElement(css_selector="a[href='/tasks/network/ddi/']")
    invent_DDI = WebElement(css_selector="a[href='/tasks/network/ddi/index/']")
    # ....Network infrastructure....#
    auth_error_Huawei = WebElement(css_selector="a[href='/tasks/infrastructure/huawei-agile-campus/auth-errors/']")
    commutator_config = WebElement(css_selector="a[href='/tasks/infrastructure/commutators/config/']")