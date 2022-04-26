from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize Chrome Session

driver = webdriver.Chrome('chromedriver')

driver.set_window_size(1024, 600)
driver.maximize_window()

executor_url = driver.command_executor._url
session_id = driver.session_id

print(session_id)
print(executor_url)

# Login via OKTA

driver.get("https://my.wpengine.com/sites")

print(driver.title)

username_login = driver.find_element_by_name("username")

username_login.clear()
username_login.send_keys("robert.li@wpengine.com")
username_login.send_keys(Keys.RETURN)

print(driver.current_url)
print(driver.title)

password_login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

password_login = driver.find_element(By.NAME, 'password')

password_login.clear()
password_login.send_keys("PWN4TXsT7xK%&@Fot*8@cN68")
password_login.send_keys(Keys.RETURN)

driver.implicitly_wait(3)   

print(driver.current_url)
print(driver.title)

okta_button = driver.find_element_by_css_selector("#form64 > div.o-form-button-bar > input").click()

# Sites Experience

sites_xp_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "sites-unicorn")))

# Access Logs Window > Download Complete Access Logs

driver.get("https://my.wpengine.com/installs/hezlr/access_logs")

access_log_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "MuiTableRow-root")))

print(driver.current_url)
print(driver.title)

csv_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/div/div[1]/div/div[2]/button").click()

log_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]")))


driver.implicitly_wait(30)

action = ActionChains(driver).move_to_element_with_offset(log_button, 100, 20)
action.click()
action.perform()

