import pickle

def save_cookies(driver, name_cookie):

    pickle.dump(driver.get_cookies(), open(name_cookie, "wb"))


def load_cookies(driver, name_cookie):
    cookies = pickle.load(open(name_cookie, "rb"))
    driver.delete_all_cookies()
    driver.get("http://172.17.127.22:3001/")
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)