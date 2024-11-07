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
# TC06: Kiểm thử đăng nhập với thông tin hợp lệ
def test_valid_login(driver):
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
    assert "http://localhost/opencartsite/index.php?route=account/login&language=en-gb" in driver.current_url
    # Nhập email vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gmail.com")
    # Nhập password vào trường nhập liệu, ở đây là "12345"
    driver.find_element(By.ID, "input-password").send_keys("12345")
    # Bấm nút Login
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']").click()
    time.sleep(3)
    assert "http://localhost/opencartsite/index.php?route=account/account&language=en-gb" in driver.current_url
