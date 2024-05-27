from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_result_page.verify_search_results(expected_item)

