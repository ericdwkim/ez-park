import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to check for existing guests info or ask for new guest's info
def existing_or_new_guest(env_var_name, prompt_msg):
    if env_var_name in os.environ:
        print(f' env_var_name: {env_var_name}')
        return os.getenv(env_var_name)
    else:
        return input(prompt_msg)

# Get initials
initials = input('Enter the guest\'s initials (eg: "JS" for John Smith): ')

# Check if env vars exist and fetch values or ask for new guest info
license_plate_env_name = f'{initials}_LICENSE_PLATE'
guest_phone_env_name = f'{initials}_CELL_NUM'

# TODO: ensure that license plate follows the general format of a typical license plate w/ odd exceptions allowed
# TODO: ensure that cell phone numbers are insensitive to inputted format for easier copy/paste as input or as just a series of ints
license_plate_to_register = existing_or_new_guest(license_plate_env_name, "Enter the guest's license plate to register: ")
guest_phone_num = existing_or_new_guest(guest_phone_env_name, "Enter the guest's cell number to register: ")


# Environmental variables
# license_plate_to_register = os.getenv('TEST_LICENSE_PLATE')
# guest_phone_num = os.getenv('TEST_CELL_NUM')

resident_parking_code = os.getenv('RESIDENT_PARKING_CODE')
# test_phone_num = os.getenv('GOOGLE_VOICE_PHONE_NUM')
parqking_url = os.getenv('PARQKING_URL')

# Chrome driver instance
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = uc.Chrome(use_subprocess=True, version_main=113, options=options)
driver.get(parqking_url)

# 1) Enter license plate
license_plate_textbox_selector = driver.find_element(By.CSS_SELECTOR, '#plateno')
license_plate_textbox_selector.click()
license_plate_textbox_selector.send_keys(license_plate_to_register)

# 2) Submit to register license plate
submit_plate_btn = driver.find_element(By.CSS_SELECTOR, '.guest-pass')
submit_plate_btn.click()

# 3) Wait for resident code pop up modal
enter_resident_code_modal_wait = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#guestCode')))

# 4) Enter resident code
enter_resident_code_modal = driver.find_element(By.CSS_SELECTOR, '#guestCode')
enter_resident_code_modal.click()
enter_resident_code_modal.send_keys(resident_parking_code)

# 5) Enter resident guest phone number
guest_phone_number_textbox_selector = driver.find_element(By.CSS_SELECTOR, '#guestphone')
guest_phone_number_textbox_selector.click()
# guest_phone_number_textbox_selector.send_keys(test_phone_num)
guest_phone_number_textbox_selector.send_keys(guest_phone_num)


# 6) Submit resident code & guest phone number
continue_btn = driver.find_element(By.CSS_SELECTOR, '#issue-guest-pass')
continue_btn.click()

# 7) Confirmation screen details
confirmation_screen_wait = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'h4.text-center:nth-child(1)')) #"PASS ISSUED"
)
guest_plate_num = driver.find_element(By.CSS_SELECTOR, 'h1.text-center')
print(f'Resident guest\'s license plate: "{guest_plate_num.text}" has been registered!')

# 8) Format web receipt url from parkit receipt url
parkit_receipt_url = driver.current_url
print(f'parkit_receipt_url: {parkit_receipt_url}') # base_url/Parkit/...
old_substr = "Parkit"
new_substr = "Web"

# Find start/end indices of substring to replace
start_idx = parkit_receipt_url.find(old_substr) # 21 idx
end_idx = start_idx + len(new_substr) # 27 idx
# Construct new url string replacing old with new substring
web_receipt_url = parkit_receipt_url[:start_idx] + new_substr + parkit_receipt_url[end_idx:]
print(f'web_receipt_url: {web_receipt_url}') # base_url/Web/...
driver.get(web_receipt_url)

# 9) Save screenshot
# license_plate_from_web_receipt = driver.find_element(By.CSS_SELECTOR, '.textLayer > span:nth-child(35)')
# registration_receipt_box = driver.save_screenshot(f'DayPassReceipt-{license_plate_from_web_receipt}.png') # `DayPassReceipt-ABC1234.png`
