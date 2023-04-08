import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Environmental variables
license_plate_to_register = os.getenv('TEST_LICENSE_PLATE')
resident_parking_code = os.getenv('RESIDENT_PARKING_CODE')
test_phone_num = os.getenv('GOOGLE_VOICE_PHONE_NUM')
parqking_url = os.getenv('PARQKING_URL')

# Chrome driver instance
options = webdriver.ChromeOptions()
driver = uc.Chrome(use_subprocess=True, version_main=111, options=options)
driver.get(parqking_url)

# license_plate_textbox_wait = WebDriverWait(driver, 15).until(
# EC.visibility_of_element_located((By.CLASS_NAME, 'form-control uppercase alphanum')))

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
guest_phone_number_textbox_selector.send_keys()


