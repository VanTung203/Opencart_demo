import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Kiểm thử chức năng THANH TOÁN
# TC22: Kiểm thử thanh toán với thông tin không hợp lệ
def test_invalid_checkout(driver):
    driver.get("http://localhost/opencartsite//")
    ''' Bước chọn sản phẩm '''
    # Thêm sản phẩm MacBook
    # Nhấp chọn "Desktops"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Desktops')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Show All Desktops"
    show_all_desktops = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=20') "
                       "and contains(text(), 'Show All Desktops')]"))
    )
    show_all_desktops.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang Show All Desktops
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=20" in driver.current_url
    # Tìm hình ảnh của MacBook bằng thuộc tính 'alt' hoặc 'title'
    palmtreopro_image = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='MacBook' and @title='MacBook']")
        )
    )
    # Cuộn đến phần tử hình ảnh MacBook để đảm bảo nó hiện trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", palmtreopro_image)
    time.sleep(1)  # Thêm thời gian chờ để cuộn hoàn tất
    # Nhấp vào hình ảnh sản phẩm để vào trang chi tiết sản phẩm
    palmtreopro_image.click()
    time.sleep(2)  # Đợi trang chi tiết sản phẩm tải
    # Tìm thanh số lượng và xóa giá trị trước khi nhập số mới
    quantity_input = driver.find_element(By.ID, "input-quantity")
    quantity_input.clear()  # Xóa giá trị hiện tại trong ô nhập liệu
    # Nhập vào thanh số lượng ngẫu nhiên (từ 1 tới 10)
    quantity_input.send_keys(str(random.randint(1, 10)))
    # Tìm nút "Add to Cart" dựa trên các thuộc tính của nút
    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart_button.click()
    time.sleep(2)
    # Nhấp chọn "Checkout"
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
    ''' Bước thanh toán '''
    # Nhấn vào lựa chọn Guest Checkout
    guest_checkout_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "input-guest"))
    )
    guest_checkout_option.click()
    time.sleep(2)
    # Điền thông tin giao hàng cho thanh toán
    driver.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys("Van")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys("Tung")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("DCT121C5user1@gmail.com")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-shipping-company").send_keys("abc")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-1").send_keys("123")
    time.sleep(1)
    # Cuộn đến phần tử "Address 2" để đảm bảo nó nằm trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2"))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2").send_keys("1")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-shipping-city").send_keys("HCM")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode").clear()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-shipping-postcode").send_keys("12345")
    time.sleep(1)
    Select(driver.find_element(By.CSS_SELECTOR, "#input-shipping-country")).select_by_visible_text("Viet Nam")  # Chọn quốc gia
    time.sleep(1)
    Select(driver.find_element(By.CSS_SELECTOR, "#input-shipping-zone")).select_by_visible_text("Ho Chi Minh City")  # Chọn vùng
    # Nhấp vào nút 'Continue'
    driver.find_element(By.CSS_SELECTOR, "#button-register").click()
    time.sleep(5)
    # Cuộn đến phần tử "Address 2" nhưng lần này ở cuối khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(false);", driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2"))
    time.sleep(5)
    # Chọn phương thức vận chuyển
    driver.find_element(By.CSS_SELECTOR, "#button-shipping-methods").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-shipping-method-flat-flat").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#button-shipping-method").click()
    time.sleep(1)
    # Chọn phương thức thanh toán
    driver.find_element(By.CSS_SELECTOR, "#button-payment-methods").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#input-payment-method-cod-cod").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#button-payment-method").click()
    time.sleep(1)
    # Cuộn xuống cuối trang
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CSS_SELECTOR, "#input-shipping-address-2"))
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#button-confirm").click()
    time.sleep(1)
    assert "http://localhost/opencartsite/index.php?route=checkout/success&language=en-gb" in driver.current_url
    # Kiểm tra xem thông báo thành công có xuất hiện không
    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Your order has been placed!"


