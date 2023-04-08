import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


license_plate_to_register = os.getenv('TEST_LICENSE_PLATE')
print(license_plate_to_register)
resident_parking_code = os.getenv('RESIDENT_PARKING_CODE')
parqking_url = os.getenv('PARQKING_URL')


options = webdriver.ChromeOptions()
driver = uc.Chrome(use_subprocess=True, version_main=111, options=options)
driver.get(parqking_url)

license_plate_textbox_wait = WebDriverWait(driver, 15).until(
EC.visibility_of_element_located((By.CLASS_NAME, 'form-control uppercase alphanum')))

license_plate_textbox_selector = driver.find_element(By.CLASS_NAME, 'form-control uppercase alphanum')
license_plate_textbox_selector.click()
license_plate_textbox_selector.send_keys(license_plate_to_register)

submit_plate_btn = driver.find_element(By.CLASS_NAME, 'guest-pass btn btn-info btn-lg btn-block btn-rounded text-uppercase waves-effect waves-light guest-pass-enter')
submit_plate_btn.click()

enter_guest_code_modal_wait = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'form-control uppercase')))
enter_guest_code_modal = driver.find_element(By.CLASS_NAME, 'form-control uppercase')
enter_guest_code_modal.click()
enter_guest_code_modal.send_keys(resident_parking_code)
