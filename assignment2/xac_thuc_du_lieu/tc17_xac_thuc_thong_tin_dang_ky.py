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

# Kiểm thử chức năng XÁC THỰC DỮ LIỆU
# TC017: Kiểm thử xác thực thông tin người dùng sau khi đăng ký tài khoản
def test_validation_user_information_after_register(driver):
    driver.get("http://localhost/opencartsite//")
    """Bước đăng ký tài khoản"""
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
    first_name = "Van Phu"
    driver.find_element(By.ID, "input-firstname").send_keys(first_name)
    # Nhập Last Name vào trường nhập liệu, ở đây là "Tung"
    last_name = "Tung"
    driver.find_element(By.ID, "input-lastname").send_keys(last_name)
    # Tạo email ngẫu nhiên
    # Nhập email vào trường nhập liệu
    random_email = f"DCT121C5user_{uuid.uuid4().hex[:8]}@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys(random_email)
    # Nhập Password vào trường nhập liệu, ở đây là "12345"
    driver.find_element(By.ID, "input-password").send_keys("12345")
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
    assert "http://localhost/opencartsite/index.php?route=account/success&language=en-gb" in driver.current_url
    """Bước Xác thực thông tin người dùng"""
    # Nhấp chọn "My Account"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "My Account"
    account_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='My Account']"))
    )
    account_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/account&language=en-gb" in driver.current_url
    # Nhấp chọn "Edit your account information" để xem thông tin tài khoản
    edit_account_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//a[contains(@href, 'route=account/edit') and contains(text(), 'Edit your account information')]")
        )
    )
    edit_account_link.click()
    time.sleep(2)
    # Lấy giá trị First Name, Last Name, E-Mail hiện có và so sánh với First Name, Last Name, E-Mail lúc đăng ký
    current_first_name = driver.find_element(By.ID, "input-firstname").get_attribute("value")
    current_last_name = driver.find_element(By.ID, "input-lastname").get_attribute("value")
    current_email = driver.find_element(By.ID, "input-email").get_attribute("value")

    # Kiểm tra thông tin First Name, Last Name và E-Mail
    assert current_first_name == first_name, f"First Name mismatch: Expected {first_name}, but got {current_first_name}"
    assert current_last_name == last_name, f"Last Name mismatch: Expected {last_name}, but got {current_last_name}"
    assert current_email == random_email, f"Email mismatch: Expected {random_email}, but got {current_email}"
