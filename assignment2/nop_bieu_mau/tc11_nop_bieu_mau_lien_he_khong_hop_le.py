import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Kiểm tra chức năng NỘP BIỂU MẪU
# TC11: Kiểm thử nộp biểu mẫu liên hệ với thông tin không hợp lệ
def test_invalid_form_submission_contact_us(driver):
    driver.get("http://localhost/opencartsite//")
    # Chờ và nhấp vào "fa-solid fa-phone"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/opencartsite/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Nhập Your Name vào trường nhập liệu, ở đây là "VanTung"
    driver.find_element(By.ID, "input-name").send_keys("VanTung")
    # Nhập email không hợp lệ vào trường nhập liệu, ở đây là "DCT121C5user1@gma*il.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gma*il.com")
    # Nhập Enquiry không hợp lệ (nằm ngoài 10-3000 ký tự) vào trường nhập liệu, ở đây là "alo123@"
    driver.find_element(By.ID, "input-enquiry").send_keys("alo123@")
    # Nhấp vào nút "Submit"
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    submit_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-enquiry").text
    assert "Enquiry must be between 10 and 3000 characters!" in error_message