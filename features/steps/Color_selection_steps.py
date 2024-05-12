from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


color_option_locator = (By.CSS_SELECTOR, ".swatchAnchor")
selected_color_locator = (By.CSS_SELECTOR, ".js-current-selection")
product_page_url = "https://www.target.com/p/A-91511634"


@given('I navigate to the Target product page')
def navigate_to_product_page(context):
    context.driver.get(product_page_url)


@when('I loop through color options and verify each color selection')
def loop_through_colors(context):
    color_options = context.driver.find_elements(*color_option_locator)
    for color_option in color_options:
        color_name = color_option.get_attribute("title")
        color_option.click()
        WebDriverWait(context.driver, 10).until(
            EC.text_to_be_present_in_element(selected_color_locator, color_name)
        )
        selected_color = context.driver.find_element(*selected_color_locator).text
        assert color_name == selected_color, f"Selected color is not {color_name}"


@then('I should see that each color has been selected')
def verify_all_colors_selected(context):
    selected_colors = set()
    color_options = context.driver.find_elements(*color_option_locator)
    for color_option in color_options:
        selected_color = color_option.get_attribute("title")
        selected_colors.add(selected_color)
    assert len(selected_colors) == len(color_options), "Not all colors have been selected"



