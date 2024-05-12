from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert '<expected_item>' in actual_text, f'Error! Text {expected_item} not in {actual_text}'

