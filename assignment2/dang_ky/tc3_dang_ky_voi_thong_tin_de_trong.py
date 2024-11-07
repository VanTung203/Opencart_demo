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

# Kiểm thử chức năng ĐĂNG KÝ
# TC03: Kiểm thử đăng ký với thông tin để trống
def test_register_with_empty_informatio(driver):
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
    # Để trống First Name
    driver.find_element(By.ID, "input-firstname").clear()
    # Để trống Last Name
    driver.find_element(By.ID, "input-lastname").clear()
    # Để trống địa chỉ email
    driver.find_element(By.ID, "input-email").clear()
    # Để trống password
    driver.find_element(By.ID, "input-password").clear()
    # Nhấp vào phần tử "agree"
    # agree_checkbox = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "//input[@type='checkbox' and @name='agree' and @value='1']"))
    # )
    # # Cuộn đến phần tử để đảm bảo nó hiện trong khung nhìn
    # driver.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)
    # time.sleep(1)  # Thêm một chút thời gian chờ để cuộn hoàn tất
    # agree_checkbox.click()
    # Chờ và nhấp vào nút "Continue"
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Continue']"))
    )
    # Cuộn đến vị trí của nút "Continue" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    continue_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-firstname").text
    assert "First Name must be between 1 and 32 characters!" in error_message
    error_message = driver.find_element(By.ID, "error-lastname").text
    assert "Last Name must be between 1 and 32 characters!" in error_message
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-password").text
    assert "Password must be between 4 and 20 characters!" in error_message
    # Chờ và lấy thông báo lỗi từ thẻ có id "alert"
    try:
        alert_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='alert']"))
        )
        error_message = alert_element.text
    except:
        error_message = ""
    # Kiểm tra nội dung thông báo lỗi
    assert "You must agree to the Privacy Policy" in error_message

