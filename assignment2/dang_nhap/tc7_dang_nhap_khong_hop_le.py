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

# Kiểm thử chức năng ĐĂNG NHẬP
# TC07: Kiểm thử đăng nhập với thông tin không hợp lệ
# (mật khẩu không hợp lệ - nằm ngoài trường 4-20 kí tự)
def test_invalid_login(driver):
    driver.get("http://localhost/opencartsite//")
    # Chờ và nhấp vào "My Account" dropdown
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    # Chờ và nhấp vào phần tử "Login"
    login_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Login']"))
    )
    login_link.click()
    # Nhập email vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gmail.com")
    # Nhập password vào trường nhập liệu, ở đây là "123" (mật khẩu không hợp lệ)
    driver.find_element(By.ID, "input-password").send_keys("123")
    # Bấm nút Login
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']").click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Chờ và lấy thông báo lỗi từ thẻ có id "alert"
    try:
        alert_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='alert']"))
        )
        error_message = alert_element.text
    except:
        error_message = ""
    # Kiểm tra tính chính xác của nội dung thông báo lỗi
    assert "No match for E-Mail Address and/or Password" in error_message