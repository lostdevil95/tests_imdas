import pytest
import psycopg2
from psycopg2 import Error
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import uuid
import logging
import sys
from pytest_reportportal import RPLogger, RPLogHandler


@pytest.fixture(scope="session")
def rp_logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    if hasattr(request.node.config, 'py_test_service'):
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    rp_handler.setLevel(logging.INFO)
    return logger


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help='chrome, firefox or opera')
    parser.addoption('--executor', action='store', default="172.17.127.22", help='selenoid_url or local')
    parser.addoption('--mobile', action='store_true')
    parser.addoption('--vnc', action='store', default=True, help='enable or disable interactive mode')
    parser.addoption('--logs', action='store', default=True, help='True or False')
    parser.addoption('--video', action='store', default=False, help='It makes video-tape of test cases')
    parser.addoption('--resolution', action='store', default="1920x1080", help='Chose resolution of the screen')


@pytest.fixture(scope='function')
def browser(request):
    browser = request.config.getoption('--browser')
    executor = request.config.getoption('--executor')
    # version = request.config.getoption('--version')
    vnc = request.config.getoption('--vnc')
    logs = request.config.getoption('--logs')
    video = request.config.getoption('--video')
    resolution = request.config.getoption('--resolution')

    if executor == 'local':
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome('/Users/sergejlavrenov/chromedriver')
        driver = webdriver.Chrome('/usr/local/share/chromedriver/chromedriver')
    else:
        executor_url = 'http://172.17.127.22:4444/wd/hub'

        caps = {
            "browserName": browser,
            "screenResolution": resolution,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": bool(video),
                "enableLog": logs
            }
        }
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
        driver.maximize_window()

    def fin():
        if request.node.rep_call.failed:
            try:
                browser.execute_script("document.body.bgColor = 'white';")
                browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
                print('URL: ', browser.current_url)
                print('Browser logs:')
                for log in browser.get_log('browser'):
                    print(log)
            except:
                pass
        driver.quit()

    request.addfinalizer(fin)
    return driver


# коннект к БД
@pytest.fixture(scope='function')
def cursor():
    try:
        connection = psycopg2.connect(
            user='imdas',
            password='12345',
            host='172.17.127.22',
            database='imdas',
            port='5434'
        )
        cursor = connection.cursor()
        yield cursor
        connection.close()
    except (Exception, Error) as e:
        return f"Ошибка при работе с PostgreSQL {e}"


def get_test_case_docstring(item):
    """ Эта функция получает строку документа из тестового набора и форматирует ее,
        чтобы показать ее вместо имени самого теста """

    full_name = ''

    if item._obj.__doc__:
        # Убирает лишние пробелы:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())
        # Генериует список параметров для параметризированных тестов:
        if hasattr(item, 'callspec'):
            params = item.callspec.params
            res_keys = sorted([k for k in params])
            # Создает словарь:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')
    return full_name


def pytest_itemcollected(item):
    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    if session.config.option.collectonly is True:
        for item in session.items:
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)
        pytest.exit('Готово!')
