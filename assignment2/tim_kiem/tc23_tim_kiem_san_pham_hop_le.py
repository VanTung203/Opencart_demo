import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Kiểm thử chức năng Tìm kiếm
# TC23: Kiểm thử tìm kiếm với đầu vào hợp lệ
def test_valid_search(driver):
    driver.get("http://localhost/opencartsite/")
    time.sleep(2)
    # Nhập từ khóa vào ô tìm kiếm
    driver.find_element(By.NAME, "search").send_keys("Macbook")
    # Click vào nút tìm kiếm
    driver.find_element(By.CLASS_NAME, "btn-light").click()
    time.sleep(2)
    # Kiểm tra từ khóa trong kết quả tìm kiếm
    assert "Macbook" in driver.page_source
