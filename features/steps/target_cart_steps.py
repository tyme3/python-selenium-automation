from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@when('Click on the Cart icon')
def click_cart_icon(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
    cart_icon.click()


@then('Verify "Your cart is empty" message is shown')
def verify_empty_cart_message(context):
    sleep(3)
    empty_cart_message = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem')
    assert empty_cart_message.text == "Your cart is empty"

    context.driver.quit()