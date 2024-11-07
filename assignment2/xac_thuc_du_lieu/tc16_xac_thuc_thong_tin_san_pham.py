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

# Kiểm thử chức năng XÁC THỰC DỮ LIỆU
# TC016: Kiểm thử xác thực thông tin chi tiết sản phẩm hiển thị đúng trên trang sản phẩm (tên, giá, mô tả)
def test_validation_product_details_displayed(driver):
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
    # Xác minh URL điều hướng tới trang PC
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
    '''Lấy thông tin sản phẩm MacBook trên trang sản phẩm'''
    # Lấy tên sản phẩm
    product_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='http://localhost/opencartsite/index.php?route=product/product&language=en-gb&product_id=43&path=20'][contains(text(), 'MacBook')]")
        )
    ).text
    # Lấy giá sản phẩm
    product_price = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='price-new' and contains(text(), '$602.00')]")
        )
    ).text
    # Lấy mô tả sản phẩm
    product_description = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(), 'Intel Core 2 Duo processor')]")
        )
    ).text
    # Nhấp vào hình ảnh sản phẩm để vào trang chi tiết sản phẩm
    macbook_image.click()
    time.sleep(2)  # Đợi trang chi tiết sản phẩm tải
    '''Lấy thông tin sản phẩm trên trang chi tiết'''
    # Lấy tên sản phẩm
    product_detail_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'MacBook')]")
        )
    ).text
    # Lấy giá sản phẩm
    product_detail_price = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='price-new' and contains(text(), '$602.00')]")
        )
    ).text
    # Tìm phần mô tả sản phẩm trong trang chi tiết sản phẩm
    description_section = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='tab-description']")  # Tìm khu vực mô tả sản phẩm
        )
    )
    # Cuộn đến phần tử mô tả sản phẩm để đảm bảo nó hiển thị trong khung nhìn
    driver.execute_script("arguments[0].scrollIntoView(true);", description_section)
    time.sleep(1)  # Thêm thời gian chờ để cuộn hoàn tất
    # Lấy mô tả sản phẩm từ trang chi tiết
    product_detail_description_elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='tab-description']//p")
        )
    )
    # Ghép các đoạn mô tả thành một chuỗi duy nhất
    product_detail_description = ' '.join([element.text for element in product_detail_description_elements])
    # So sánh thông tin giữa trang sản phẩm và trang chi tiết sản phẩm
    assert product_name == product_detail_name, f"Tên sản phẩm không khớp! Expected '{product_name}' but got '{product_detail_name}'"
    assert product_price == product_detail_price, f"Giá sản phẩm không khớp! Expected '{product_price}' but got '{product_detail_price}'"
    # Kiểm tra mô tả sản phẩm ngắn có nằm trong mô tả chi tiết
    product_description_clean = ' '.join(product_description.split())  # Loại bỏ khoảng trắng thừa
    product_detail_description_clean = ' '.join(product_detail_description.split())  # Loại bỏ khoảng trắng thừa
    # Chỉ lấy phần đầu của mô tả ngắn (ví dụ: 10 từ đầu tiên) để so sánh
    product_description_words = product_description_clean.split()[:10]
    short_product_description = ' '.join(product_description_words)
    # Kiểm tra phần mô tả đã rút gọn có nằm trong mô tả chi tiết không
    assert short_product_description in product_detail_description_clean, \
        f"Mô tả sản phẩm không khớp! Expected part of '{short_product_description}' but got '{product_detail_description_clean}'"
    # In kết quả thông tin sản phẩm
    # print("Thông tin sản phẩm trên trang sản phẩm:")
    # print(f"Tên sản phẩm: {product_name}")
    # print(f"Giá sản phẩm: {product_price}")
    # print(f"Mô tả sản phẩm: {product_description}")
    # print("Thông tin sản phẩm trên trang chi tiết sản phẩm:")
    # print(f"Tên sản phẩm: {product_detail_name}")
    # print(f"Giá sản phẩm: {product_detail_price}")
    # print(f"Mô tả sản phẩm: {product_detail_description}")

