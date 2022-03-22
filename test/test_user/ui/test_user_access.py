import settings
from pages.user.user_main_page import UserMainPage
from pages.auth_page import AuthPage
import pytest
from pages.cookies import save_cookies, load_cookies
from time import sleep


def test_user_login(browser, rp_logger):
    '''Логинимся'''
    rp_logger.info('CASE - Логин от пользователя')
    page = AuthPage(browser)
    page.login.send_keys(settings.USER)
    page.password.send_keys(settings.PASSWORD)
    page.enter.click()
    sleep(5)
    rp_logger.info('Сохраняем куки файл в корневую дирректорию с названием "cookie_user" ')
    save_cookies(browser, 'cookie_user')
    assert page.get_current_url() == 'http://172.17.127.22:3001/', 'Неуспешный вход'

@pytest.mark.skip
def test_user_not_see_cat_set(browser, rp_logger):
    '''Видны ли Юзеру каталоги и настройки'''
    rp_logger.info('CASE - Видны ли Юзеру каталоги и настройки')
    rp_logger.info('Вызов функции "test_user_login" для авторизации')
    test_user_login(browser, rp_logger)
    page = UserMainPage(browser)

    cat = page.catalogs.is_visible()
    set = page.settings.is_visible()

    assert not cat and not set, 'Пользователю видны недопустимые разделы'

def test_user_logs(browser, rp_logger):
    '''Пользователь должен иметь доступ к журналам(логам)'''
    rp_logger.info('CASE - Доступен ли журнал')
    rp_logger.info('Проброс куки')
    load_cookies(browser, 'cookie_user')
    page = UserMainPage(browser)

    page.logs.click()
    assert page.get_current_url() == 'http://172.17.127.22:3001/logs/tasks/' and page.check_logs.is_visible(), \
                        'Нет доступа к журналам(логам)'