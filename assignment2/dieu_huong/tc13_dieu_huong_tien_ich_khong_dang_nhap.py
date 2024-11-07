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

# Kiểm thử chức năng ĐIỀU HƯỚNG
# TC13: Kiểm thử điều hướng tiện ích khi không đăng nhập
def test_navigation_top_not_login(driver):
    driver.get("http://localhost/opencartsite//")
    time.sleep(2)
    # Nhấp chọn "Contact Us"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Nhấp chọn "My Account"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Register"
    register_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Register']"))
    )
    register_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/register&language=en-gb" in driver.current_url
    # Nhấp chọn "My Account"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Login"
    login_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Login']"))
    )
    login_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/login&language=en-gb" in driver.current_url
    # Nhấp chọn "Wish List"
    wish_list_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "wishlist-total"))
    )
    wish_list_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/login&language=en-gb" in driver.current_url
    # Nhấp chọn "Shopping Cart"
    shopping_cart_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Shopping Cart']"))
    )
    shopping_cart_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=checkout/cart&language=en-gb" in driver.current_url
    # Nhấp chọn "Checkout"
    checkout_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Checkout']"))
    )
    checkout_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=checkout/cart&language=en-gb" in driver.current_url