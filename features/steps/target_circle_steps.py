from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

Target_Circle = (By.CSS_SELECTOR, "a#utilityNav-circle")
benefit_cells_locator = (By.CSS_SELECTOR, "div.styles__CellItemContainer-sc-3f68hg-5.uAfgQ")


@given('I am on the Target Circle page')
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")





@then('I should see {expected_amount} benefit cells displayed')
def verify_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    benefit_cells = context.driver.find_elements(*benefit_cells_locator)
    assert len(benefit_cells) == expected_amount, f'Expected {expected_amount} benefit cells but got {len(benefit_cells)}'
