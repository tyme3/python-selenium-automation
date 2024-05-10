from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.target.com/")


signin_button = driver.find_element(By.XPATH, "//span[contains(@class, 'styles__LinkText-sc-1e1g60c-3') and text()='Sign in']")
signin_button.click()
sleep(2)


signin_side_nav = driver.find_element(By.XPATH, "//span[contains(@class, 'styles__ListItemText-sc-diphzn-1') and text()='Sign in']")
signin_side_nav.click()
sleep(2)

signin_text_element = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']")
signin_text = signin_text_element.text

sleep(2)

# Verification
expected_text = 'Sign in'
assert expected_text in signin_text, f'Expected {expected_text} but got {signin_text}'
print("Test Passed: SignIn page opened successfully.")




