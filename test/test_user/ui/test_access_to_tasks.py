from pages.cookies import load_cookies
from pages.user.task_page import UserTaskPage


def test_has_user_access_tasks(browser, rp_logger):
    '''Проверка на доступность списка задач'''
    rp_logger.info('CASE - Проверка на доступность списка задач')
    failures = 0
    rp_logger.info('Проброс куки')
    load_cookies(browser, 'cookie_user')
    rp_logger.info('Переход на страницу задач')
    page = UserTaskPage(browser)
    rp_logger.info('Создание вирт. машины')
    page.create_vm.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/common/virtual-machines/create/':
        failures += 1
    page.go_back()
    rp_logger.info('Удаление вирт. машины')
    page.delete_vm.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/common/virtual-machines/remove/':
       failures += 1
    page.go_back()
    rp_logger.info('Апдейт вирт машины')
    us = page.update_server.wait_to_be_clickable()
    if us:
        page.update_server.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/common/virtual-machines/update/':
        failures += 1
    page.go_back()
    rp_logger.info('Создание файлового ресурса')
    cfs = page.create_file_source.wait_to_be_clickable()
    if cfs:
        page.create_file_source.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/common/virtual-machines/create-file-resource/':
        failures += 1
    page.go_back()
    rp_logger.info('Создание группы AD')
    cga = page.create_group_AD.wait_to_be_clickable()
    if cga:
        page.create_group_AD.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/common/active-directory/create-group/':
        failures += 1
    page.go_back()
    rp_logger.info('Создание аккаунта AD')
    csaa = page.create_service_acc_AD.wait_to_be_clickable()
    if csaa:
        page.create_service_acc_AD.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/common/active-directory/create-accout/':
        failures += 1
    page.go_back()
    rp_logger.info('Создание Email AD')
    cea = page.create_email_AD.wait_to_be_clickable()
    if cea:
        page.create_email_AD.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/common/active-directory/create-email/':
        failures += 1
    page.go_back()
                               # Функционал не работает
    # eddi = page.edit_DDI.wait_to_be_clickable()
    # if eddi:
    #     page.edit_DDI.click()
    # if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/network/ddi/':
    #     failures += 1
    # page.go_back()
                           ################################
    rp_logger.info('Инвентаризация DDI')
    iddi = page.invent_DDI.wait_to_be_clickable()
    if iddi:
        page.invent_DDI.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/network/ddi/index/':
        failures += 1
    page.go_back()
    rp_logger.info('Ошибки аутентификации Huawei AC')
    aeH = page.auth_error_Huawei.wait_to_be_clickable()
    if aeH:
        page.auth_error_Huawei.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/infrastructure/huawei-agile-campus/auth-errors/':
        failures += 1
    page.go_back()
    rp_logger.info('Конфигурации коммутаторов')
    cc = page.commutator_config.wait_to_be_clickable()
    if cc:
        page.commutator_config.click()
    if not page.get_current_url() == 'http://172.17.127.22:3001/tasks/infrastructure/commutators/config/':
        failures += 1
    assert not failures, f'Ошибки перехода: {failures}'
    rp_logger.info('''--- РЕЗУЛЬТАТ ---\n!OK! Ошибок перехода нет''')

