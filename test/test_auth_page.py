from pages.auth_page import AuthPage
from settings import USER, ADMIN, SECURITY, USER_ADMIN, USER_ADMIN_SECURITY, PASSWORD
import pytest

@pytest.mark.skip
def test_can_access_not_login(browser, rp_logger):
    '''Проверка на доступность сервиса без авторизации'''
    rp_logger.info('CASE - Проверка на доступность сервиса без авторизации')
    page = AuthPage(browser)
    page.imdas.click()
    assert page.get_current_url() != 'http://172.17.127.22:3001'
@pytest.mark.skip
@pytest.mark.parametrize('login, psw', [
                                        (USER, PASSWORD),
                                        (ADMIN, PASSWORD),
                                        (SECURITY, PASSWORD),
                                        (USER_ADMIN, PASSWORD),
                                        (USER_ADMIN_SECURITY, PASSWORD)
                                        ]
                         )
def test_login_positive(login, psw, rp_logger, browser):
    '''Логинимся'''
    rp_logger.info('CASE - Параметризированный вход на ресурс с правильными данными')
    page = AuthPage(browser)
    page.login.send_keys(login)
    page.password.send_keys(psw)
    page.enter.click()
    assert page.get_current_url() == 'http://172.17.127.22:3001/', 'Неуспешный вход'

@pytest.mark.parametrize('login, psw', [
                                        (USER, 'QAZ2wsx'),
                                        (ADMIN, '!QAZ2ws'),
                                        (SECURITY, '!QAZwsx'),
                                        (USER_ADMIN, '!QAZ2wx'),
                                        (USER_ADMIN_SECURITY, '!QAZ2wsх'),
                                        ('user', PASSWORD),
                                        ('user_2', PASSWORD),
                                        ('user 3', PASSWORD),
                                        ('user.4', PASSWORD)
                                        ]
                         )
def test_login_negative(login, psw, rp_logger, browser):
    '''Логинимся'''
    rp_logger.info('CASE - Параметризированный вход на ресурс с неправильными данными')
    page = AuthPage(browser)
    page.login.send_keys(login)
    page.password.send_keys(psw)
    page.enter.click()
    assert page.get_current_url() != 'http://172.17.127.22:3001/', 'Вход произошел, но не должен был'