from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#get the path to the ChromeDrive executable
driver_path= ChromeDriverManager().install()




#Create a new Chrome Browser instance
service= Service(driver_path)
driver = webdriver.Chrome(service=service)
drive.maximize_window()

#open the url
driver.get('https://www.amazoncom/')


# By CSS, ID
driver.find_element(By.CSS_Selector, "#twotabsearchtextbox")

# By CSS, classes
driver.find_element(By.CSS_Selector, "input.nav-progressive-attribute")
driver.find_element(By.CSS_Selector, "input.nav-input.nav-progressive-attribute")
driver.find_element(By.CSS_Selector, ".nav-input.nav-progressive-attribute")
driver.find_element(By.CSS_Selector, "twotabsearchtextbox.nav-input")

#By CSS, Attributes
driver.find_element(By.CSS_Selector, "input[placeholder='Search Amazon']")
driver.find_element(By.CSS_Selector, "[placeholder = 'Search Amazon']")
driver.find_element(By.CSS_Selector, "twotabsearchtextbox.nav-input[placeholder='Search Amazon']")

#By CSS, multiple attributes
driver.find_element(By.CSS_Selector, "input[placeholder='Search Amazon'][type='text']")

#contains *=
driver.find_element(By.CSS_Selector, "a[href*='topnav_lang']")
#from target, contains *= for a class
driver.find_element(By.CSS_Selector, "h1[class*='StyledHeading']")