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

# Kiểm thử chức năng ĐĂNG XUẤT
# TC09: Kiểm thử đăng xuất thành công sau khi đã đăng nhập
def test_successful_logout(driver):
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
    time.sleep(3)
    # Nhập email vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gmail.com")
    # Nhập password vào trường nhập liệu, ở đây là "12345"
    driver.find_element(By.ID, "input-password").send_keys("12345")
    # Bấm nút Login
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']").click()
    time.sleep(3)
    assert "http://localhost/opencartsite/index.php?route=account/account&language=en-gb" in driver.current_url
    # Chờ và nhấp vào "My Account" dropdown
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    # Chờ và nhấp vào phần tử "Logout"
    logout_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Logout']"))
    )
    logout_link.click()
    time.sleep(3)
    assert "http://localhost/opencartsite/index.php?route=account/logout&language=en-gb" in driver.current_url
