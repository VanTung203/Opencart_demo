import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Kiểm thử chức năng THÊM VÀO GIỎ HÀNG
# TC19: Kiểm thử thêm sản phẩm với số lượng nhiều vào giỏ hàng
def test_add_to_cart_1_product_with_large_quantity(driver):
    driver.get("http://localhost/opencartsite//")
    ''' Bước chọn sản phẩm '''
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
    macbook_image = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='MacBook' and @title='MacBook']")
        )
    )
    # Cuộn đến phần tử hình ảnh MacBook để đảm bảo nó hiện trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", macbook_image)
    time.sleep(1)  # Thêm thời gian chờ để cuộn hoàn tất
    # Nhấp vào hình ảnh sản phẩm để vào trang chi tiết sản phẩm
    macbook_image.click()
    time.sleep(2)  # Đợi trang chi tiết sản phẩm tải
    # Tìm thanh số lượng và xóa giá trị trước khi nhập số mới
    quantity_input = driver.find_element(By.ID, "input-quantity")
    quantity_input.clear()  # Xóa giá trị hiện tại trong ô nhập liệu
    # Nhập vào thanh số lượng ngẫu nhiên (từ 2 tới 10)
    quantity_input.send_keys(str(random.randint(2, 10)))
    # Tìm nút "Add to Cart" dựa trên các thuộc tính của nút
    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart_button.click()
    time.sleep(2)
    # Nhấp chọn "Shopping Cart"
    shopping_cart_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Shopping Cart']"))
    )
    # Cuộn đến phần tử "Shopping Cart" để đảm bảo nó hiện trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", shopping_cart_link)
    time.sleep(5)  # Thêm thời gian chờ để cuộn hoàn tất
    # Nhấp vào nút "Shopping Cart"
    shopping_cart_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=checkout/cart&language=en-gb" in driver.current_url