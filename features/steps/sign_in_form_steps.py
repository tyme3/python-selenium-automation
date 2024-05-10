from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('Click Sign In')
def click_sign_in(context):
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, 'span.styles__LinkText-sc-1e1g60c-3.dZfgoT.h-margin-r-x3')
    sign_in_link.click()

@when('Click Sign In from the right side navigation menu')
def click_sign_in_from_menu(context):
    sign_in_menu_item = context.driver.find_element(By.CSS_SELECTOR, 'span.styles__ListItemText-sc-diphzn-1.jaMNVl')
    sign_in_menu_item.click()


@then('Verify Sign In form is opened')
def verify_sign_in_form_opened(context):
    sign_in_form = context.driver.find_element(By.CSS_SELECTOR, 'div.styles__AuthContainerWrapper-sc-19gc5cv-2.jYGMyH')
    assert sign_in_form.is_displayed()

    # Close the browser after the test
    context.driver.quit()

