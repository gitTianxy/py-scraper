# encoding=utf-8
"""
selenium demo
---------------------
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_in_chrome(url):
    """
    The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully 
    loaded (that is, the “onload” event has fired) before returning control to your test or script. 
    
    It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely 
    loaded.
    :param url: 
    :return: 
    """
    browser = webdriver.Chrome()
    browser.get(url)


def elem_interactive():
    """
    input box, select-options
    """
    # params
    url = 'https://www.python.org'
    elem_name = 'id'
    elem_val = 'id-search-field'
    attr_name = 'type'
    # find element
    driver = webdriver.Chrome()
    driver.get(url)
    elem = None
    find_elem_code = "elem=driver.find_element_by_%s('%s')" % (elem_name, elem_val)
    exec find_elem_code
    if not elem:
        raise RuntimeError('element does not exist')
    # get attributes of element
    attr_val = elem.get_attribute(attr_name)
    print 'attr: %s=%s' % (attr_name, attr_val)
    # input/clear/submit
    elem.send_keys('test input')
    elem.clear()
    elem.send_keys('search test', Keys.RETURN)
    # jump back -- test
    page_jump(driver, 'B')


def page_jump(driver, action):
    """
    jump forward or backward, refresh;
    """
    if 'F' == action:
        driver.forward()
    elif 'B' == action:
        driver.back()
    elif 'R' == action:
        driver.refresh()


def page_wait_until():
    """
    wait util -- value of 'selenium.webdriver.support.expected_conditions':
        title_is
        title_contains
        presence_of_element_located
        visibility_of_element_located
        visibility_of
        presence_of_all_elements_located
        text_to_be_present_in_element
        text_to_be_present_in_element_value
        frame_to_be_available_and_switch_to_it
        invisibility_of_element_located
        element_to_be_clickable – it is Displayed and Enabled.
        staleness_of
        element_to_be_selected
        element_located_to_be_selected
        element_selection_state_to_be
        element_located_selection_state_to_be
        alert_is_present
    """
    # dependencies
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    # params
    url = 'https://www.python.org'
    wait_secs = 10
    elem_id = 'id-search-field'
    # actions
    driver = webdriver.Chrome()
    driver.get(url)
    elem = None
    try:
        elem = WebDriverWait(driver, wait_secs).until(
            EC.presence_of_element_located((By.ID, elem_id))
        )
    except Exception, e:
        print e
    finally:
        if elem:
            print 'find element %s, now start doing search' % elem.get_attribute('type')
            elem.send_keys('search test', Keys.RETURN)
        else:
            print 'element not loaded within %s seconds' % wait_secs
        driver.quit()


def cookie_operation():
    """
    add/get cookies
    """
    # params
    url = 'https://www.python.org'
    # actions: add, get, get_all
    driver = webdriver.Chrome()
    driver.get(url)
    driver.add_cookie(dict(name='name_test', value='kevin'))
    driver.add_cookie(dict(name='passwd_test', value='1234'))
    print 'cookie[name_test]: %s' % (driver.get_cookie('name_test'))
    for cookie in driver.get_cookies():
        print cookie


def findinputbox_and_sendkeys(url, elem_id=None, elem_name=None, elem_cls=None):
    """
    api methods:
        1. driver.title: get page title
        2. driver.find_element_by_*: get element by *
        3. driver.page_source: return page content
        4. elem.send_keys: send keys to input box; usually for automatically search test
    :param url:
    :param elem_id:
    :param elem_name:
    :param elem_cls:
    :return:
    """
    driver = webdriver.Chrome()
    driver.get(url)
    assert "Python" in driver.title
    if elem_id:
        elem = driver.find_element_by_id(elem_id)
    elif elem_name:
        elem = driver.find_element_by_name(elem_name)
    elif elem_cls:
        elem = driver.find_element_by_class_name(elem_cls)
    else:
        raise RuntimeError('the element name should only be id, name or class')
    elem.send_keys("pycon", Keys.RETURN)
    print driver.page_source


if __name__ == '__main__':
    # open_in_chrome('https://www.baidu.com')
    # findinputbox_and_sendkeys('https://www.python.org', elem_name='q')
    # elem_interactive()
    # page_wait_until()
    # cookie_operation()
    pass
