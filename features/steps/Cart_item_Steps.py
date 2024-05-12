from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Define the locators
keyword_input_locator = (By.CSS_SELECTOR, "input[data-test='@web/Search/SearchInput']")
cart_locator = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
add_to_cart_locator = (By.CSS_SELECTOR, ".styles__ButtonPrimary-sc-5fh6rr-0")
confirm_add_to_cart_locator = (By.CSS_SELECTOR, "button[data-test='shippingButton']")
view_cart_locator = (By.XPATH, "//a[contains(text(), 'View cart & check out')]")
cart_item_locator = (By.CSS_SELECTOR, "div[data-test='cartItem-title']")
remove_item_locator = (By.CSS_SELECTOR, "button[data-test='cartItem-deleteBtn']")


@given('I am on the Target website')
def target_site(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")


@when('I search for "{keyword}"')
def search_for_product(context, keyword):
    keyword_input = context.driver.find_element(*keyword_input_locator)
    keyword_input.clear()
    keyword_input.send_keys(keyword)
    keyword_input.send_keys(Keys.RETURN)


@when('I add the first {item} to my cart')
def add_item_to_cart(context, item):
    sleep(6)
    add_button = context.driver.find_element(*add_to_cart_locator)
    add_button.click()
    confirm_button = context.driver.find_element(*confirm_add_to_cart_locator)
    confirm_button.click()


@then('I should see the "{expected_item}" in my cart')
def verify_item_in_cart(context, expected_item):
    sleep(2)
    context.driver.find_element(*view_cart_locator).click()
    sleep(2)
    cart_item = context.driver.find_element(*cart_item_locator)
    assert expected_item in cart_item.text, f"{expected_item} not found in cart"

    context.driver.find_element(*remove_item_locator).click()
    context.driver.quit()