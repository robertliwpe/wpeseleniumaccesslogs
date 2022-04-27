from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import linecache

# Importing Global Vars & Install List Array

globvars_uname = linecache.getline('globalvars.txt', 2)
globvars_pw = linecache.getline('globalvars.txt', 4)
install_list = linecache.getline('installlist.txt', 2)

install_list_arr = install_list.split()

# Initialize Chrome Session

driver = webdriver.Chrome('chromedriver')

driver.set_window_size(1024, 600)
driver.maximize_window()

executor_url = driver.command_executor._url
session_id = driver.session_id

print("Establishing Local Webdriver Instance...")
print(session_id)
print(executor_url)

print(f"\nFor User:")
print(globvars_uname)

print("For Installs:")
print(install_list_arr)

print(f"\n========== ACTIONS START ==========")

# Login

driver.get("https://my.wpengine.com/sites")

print(driver.title)

#username_login = driver.find_element_by_name("username")
username_login = driver.find_element(By.NAME, "username")

username_login.clear()
username_login.send_keys(globvars_uname)
# username_login.send_keys(Keys.RETURN)

print(driver.current_url)

password_login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

password_login = driver.find_element(By.NAME, 'password')

password_login.clear()
password_login.send_keys(globvars_pw)
# password_login.send_keys(Keys.RETURN)

driver.implicitly_wait(3)   

print(driver.current_url)
print(driver.title)

# OKTA for WPE Employee Login

if "sso/saml" in driver.current_url:
    print("Open your MFA App to Verify Login")
    #okta_button = driver.find_element_by_css_selector("#form64 > div.o-form-button-bar > input").click()
    okta_button = driver.find_element(By.CSS_SELECTOR, "#form64 > div.o-form-button-bar > input")
    okta_button.click()
else:
    pass

# Sites Experience

sites_xp_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "sites-unicorn")))

# Access Logs Window > Download Complete Access Logs

for install_name in install_list_arr:
    install_string = "https://my.wpengine.com/installs/{}/access_logs".format(install_name)
    driver.get(install_string)
    access_log_wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "MuiTableRow-root")))
    
    print(driver.title)
    print(driver.current_url)
    
    # csv_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/div/div[1]/div/div[2]/button").click()
    csv_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div/div/div[1]/div/div[2]/button")
    csv_button.click()

    log_button_wait = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-16ldzwl")))

    # log_button = driver.find_element_by_xpath("/html/body/div[3]/div[3]/ul/li[2]")
    log_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]")

    driver.implicitly_wait(3)

    action = ActionChains(driver).move_to_element_with_offset(log_button, 100, 20)
    action.click()
    action.perform()

    driver.implicitly_wait(3)