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
# TC24: Kiểm thử tìm kiếm với đầu vào không hợp lệ
def test_invalid_search(driver):
    driver.get("http://localhost/opencartsite/")
    time.sleep(2)
    # Nhập từ khóa không hợp lệ vào ô tìm kiếm
    driver.find_element(By.NAME, "search").send_keys("abc123@*")
    # Click vào nút tìm kiếm
    driver.find_element(By.CLASS_NAME, "btn-light").click()
    time.sleep(2)
    # Kiểm tra từ khóa không hợp lệ trong kết quả tìm kiếm
    assert "abc123@*" in driver.page_source
    # Kiểm tra thông báo "There is no product that matches the search criteria."
    assert "There is no product that matches the search criteria." in driver.page_source


