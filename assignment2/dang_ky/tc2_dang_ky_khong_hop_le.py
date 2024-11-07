import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import uuid

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Kiểm thử chức năng ĐĂNG KÝ
# TC02: Kiểm thử đăng ký với thông tin không hợp lệ
def test_invalid_register(driver):
    driver.get("http://localhost/opencartsite//")
    # Chờ và nhấp vào "My Account" dropdown
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    # Chờ và nhấp vào phần tử "Register"
    register_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Register']"))
    )
    register_link.click()
    assert "http://localhost/opencartsite/index.php?route=account/register&language=en-gb" in driver.current_url
    # Nhập First Name vào trường nhập liệu, ở đây là "Van Phu"
    driver.find_element(By.ID, "input-firstname").send_keys("Van Phu")
    # Nhập Last Name vào trường nhập liệu, ở đây là "Tung"
    driver.find_element(By.ID, "input-lastname").send_keys("Tung")
    # Tạo email ngẫu nhiên
    # Nhập email vào trường nhập liệu
    random_email = f"DCT121C5user_{uuid.uuid4().hex[:8]}@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys(random_email)
    # Nhập Password không hợp lệ (thỏa 4-20 kí tự) vào trường nhập liệu, ở đây là "123"
    driver.find_element(By.ID, "input-password").send_keys("123")
    # Nhấp vào phần tử "agree"
    agree_checkbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='checkbox' and @name='agree' and @value='1']"))
    )
    # Cuộn đến phần tử để đảm bảo nó hiện trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)
    time.sleep(1)  # Thêm một chút thời gian chờ để cuộn hoàn tất
    agree_checkbox.click()
    # Chờ và nhấp vào nút "Continue"
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Continue']"))
    )
    continue_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-password").text
    assert "Password must be between 4 and 20 characters!" in error_message

