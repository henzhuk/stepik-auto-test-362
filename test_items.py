from selenium import webdriver
import pytest
import time

try: 

def test_should_check_if_add_button_found(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), 'ADD button is abscent!'

finally:

    time.sleep(5)
    browser.quit()

