from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Define the locators
keyword_input_locator = (By.CSS_SELECTOR, "input[data-test='@web/Search/SearchInput']")
cart_locator = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
add_to_cart_locator = (By.CSS_SELECTOR, ".styles__ButtonPrimary-sc-5fh6rr-0")
confirm_add_to_cart_locator = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
view_cart_locator = (By.XPATH, "//a[contains(text(), 'View cart & check out')]")
cart_item_locator = (By.CSS_SELECTOR, "div[data-test='cartItem-title']")
remove_item_locator = (By.CSS_SELECTOR, "button[data-test='cartItem-deleteBtn']")
empty_cart_message_locator = (By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem")


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart_message(context):
    sleep(2)
    empty_cart_message = context.driver.find_element(*empty_cart_message_locator).text
    assert empty_cart_message == "Your cart is empty", "Empty cart message not found"


@when('Search for water')
def search_for_product(context):
    keyword_input = context.driver.find_element(*keyword_input_locator)
    keyword_input.clear()
    keyword_input.send_keys("water")
    keyword_input.send_keys(Keys.RETURN)


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(6)
    add_button = context.driver.find_element(*add_to_cart_locator)
    add_button.click()


@when('Store product name')
def store_product_name(context):
    # You can implement storing product name logic here if needed
    pass


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    confirm_button = context.driver.find_element(*confirm_add_to_cart_locator)
    confirm_button.click()


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*view_cart_locator).click()


@then('Verify cart has 1 item(s)')
def verify_cart_has_one_item(context):
    sleep(2)
    assert len(context.driver.find_elements(*cart_item_locator)) == 1, "Cart does not have 1 item"


@then('Verify cart has correct product')
def verify_correct_product_in_cart(context):
    expected_item = "water"  # You can replace this with any expected item
    sleep(2)
    cart_item = context.driver.find_element(*cart_item_locator)
    assert expected_item in cart_item.text, f"{expected_item} not found in cart"


@then('Verify cart has "{expected_item}"')
def verify_item_in_cart(context, expected_item):
    sleep(2)
    cart_item = context.driver.find_element(*cart_item_locator)
    assert expected_item in cart_item.text, f"{expected_item} not found in cart"

    context.driver.find_element(*remove_item_locator).click()
    context.driver.quit()

