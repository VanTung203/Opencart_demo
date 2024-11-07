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
# TC14: Kiểm thử điều hướng tiện ích khi đã đăng nhập
def test_navigation_top_login(driver):
    driver.get("http://localhost/opencartsite//")
    time.sleep(2)
    '''Bước đăng nhập '''
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
    '''Xong bước đăng nhập ngoài lề'''
    '''Nhấp chọn "Contact Us"'''
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=information/contact&language=en-gb" in driver.current_url
    '''Nhấp chọn “My Account”'''
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
    '''Nhấp chọn “Order History”'''
    # Nhấp chọn "My Account"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Order History"
    order_history_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Order History']"))
    )
    order_history_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/order&language=en-gb" in driver.current_url
    '''Nhấp chọn “Transactions”'''
    # Nhấp chọn "My Account"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Transactions"
    transactions_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Transactions']"))
    )
    transactions_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/transaction&language=en-gb" in driver.current_url
    '''Nhấp chọn “Dowloads”'''
    # Nhấp chọn "My Account"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Dowloads"
    downloads_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Downloads']"))
    )
    downloads_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/download&language=en-gb" in driver.current_url
    '''Nhấp chọn "Wish List"'''
    wish_list_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "wishlist-total"))
    )
    wish_list_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=account/wishlist&language=en-gb" in driver.current_url
    '''Nhấp chọn "Shopping Cart"'''
    shopping_cart_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Shopping Cart']"))
    )
    shopping_cart_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=checkout/cart&language=en-gb" in driver.current_url
    '''Nhấp chọn "Checkout'''
    # Nhấp vào hình ảnh opencart dựa trên thuộc tính title = 'Your store'
    image_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@title='Your Store']"))
    )
    image_element.click()
    # Tìm nút "Add to Cart" dựa trên các thuộc tính của nút
    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @title='Add to Cart']")
        )
    )
    # Cuộn đến phần tử "Add to Cart" để đảm bảo nó hiện trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(1)  # Thêm thời gian chờ để cuộn hoàn tất
    # Nhấp vào nút "Add to Cart"
    add_to_cart_button.click()
    # Nhấp chọn "Checkout
    checkout_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Checkout']"))
    )
    # Cuộn đến phần tử "Checkout" để đảm bảo nó hiện trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_link)
    time.sleep(5)  # Thêm thời gian chờ để cuộn hoàn tất
    # Nhấp vào nút "Checkout"
    checkout_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=checkout/checkout&language=en-gb" in driver.current_url
