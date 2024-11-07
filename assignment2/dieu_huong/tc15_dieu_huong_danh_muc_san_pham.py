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
# TC15: Kiểm thử điều hướng các trang danh mục sản phẩm
def test_navigation_menu(driver):
    driver.get("http://localhost/opencartsite//")
    time.sleep(2)
    ''' Danh mục Desktops'''
    ''' Nhấp chọn "PC" '''
    # Nhấp chọn "Desktops"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Desktops')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "PC"
    pc_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=20_26') and contains(text(), 'PC')]"))
    )
    pc_link.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang PC
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=20_26" in driver.current_url
    ''' Nhấp chọn "Mac" '''
    # Nhấp chọn "Desktops"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Desktops')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Mac"
    mac_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=20_27') and contains(text(), 'Mac')]"))
    )
    mac_link.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang Mac
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=20_27" in driver.current_url
    ''' Nhấp chọn "Show All Desktops" '''
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
    # Xác minh URL điều hướng tới trang Show All Desktop
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=20" in driver.current_url
    ''' Danh mục Laptops & Notebooks '''
    ''' Nhấp chọn "Macs" '''
    # Nhấp chọn "Laptops & Notebooks"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Laptops & Notebooks')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Macs"
    macs_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=18_46') and contains(text(), 'Macs')]"))
    )
    macs_link.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang PC
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=18_46" in driver.current_url
    ''' Nhấp chọn "Windows" '''
    # Nhấp chọn "Laptops & Notebooks"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Laptops & Notebooks')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Windows"
    windows_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=18_45') "
                       "and contains(text(), 'Windows')]"))
    )
    windows_link.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang PC
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=18_45" in driver.current_url
    ''' Nhấp chọn "Show All Laptops & Notebooks" '''
    # Nhấp chọn "Laptops & Notebooks"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Laptops & Notebooks')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Show All Laptops & Notebooks"
    show_all_laptops_notebooks = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=18') "
                       "and contains(text(), 'Show All Laptops & Notebooks')]"))
    )
    show_all_laptops_notebooks.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang PC
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=18" in driver.current_url
    ''' Danh mục Components'''
    ''' Nhấp chọn "Show All Components" '''
    # Nhấp chọn "Components"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Components')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Show All Components"
    show_all_components = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=25') "
                       "and contains(text(), 'Show All Components')]"))
    )
    show_all_components.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang "Show All Components"
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=25" in driver.current_url
    ''' Danh mục Tablets'''
    # Nhấp chọn "Tablets"
    tablets_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=57') "
                       "and contains(text(), 'Tablets')]"))
    )
    tablets_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=57" in driver.current_url
    ''' Danh mục Software'''
    # Nhấp chọn "Software"
    software_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=17') "
                       "and contains(text(), 'Software')]"))
    )
    software_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=17" in driver.current_url
    ''' Danh mục Phones & PDAs'''
    # Nhấp chọn "Phones & PDAs"
    phonespdas_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=24') "
                       "and contains(text(), 'Phones & PDAs')]"))
    )
    phonespdas_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=24" in driver.current_url
    ''' Danh mục Cameras'''
    # Nhấp chọn "Cameras"
    cameras_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=33') "
                       "and contains(text(), 'Cameras')]"))
    )
    cameras_link.click()
    time.sleep(2)
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=33" in driver.current_url
    ''' Danh mục MP3 Players'''
    # Nhấp chọn "MP3 Players"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'MP3 Players')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Chờ và nhấp vào phần tử "Show All MP3 Players"
    show_all_mp3players = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=34') "
                       "and contains(text(), 'Show All MP3 Players')]"))
    )
    show_all_mp3players.click()
    time.sleep(2)
    # Xác minh URL điều hướng tới trang "Show All MP3 Players"
    assert "http://localhost/opencartsite/index.php?route=product/category&language=en-gb&path=34" in driver.current_url