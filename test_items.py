from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   

import pytest
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_find_add_button(browser):
    browser.get(link)
    time.sleep(5)

    button = browser.find_element_by_css_selector('.btn-add-to-basket')
   
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), 'No such button!'

    #assert [type='submitt'], 'No such button!'

    #pagination_block = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
    #                (By.CSS_SELECTOR, "button.btn-add-to-basket")))


time.sleep(5)




 

