import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import uuid
import random
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Kiểm thử chức năng ĐĂNG KÝ
# TC01: Kiểm thử đăng ký với thông tin hợp lệ
def test_valid_register(driver):
    driver.get("http://localhost/opencartsite//")
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
    driver.find_element(By.ID, "input-firstname").send_keys("Van Phu")
    # Nhập Last Name vào trường nhập liệu, ở đây là "Tung"
    driver.find_element(By.ID, "input-lastname").send_keys("Tung")
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

# TC02: Kiểm thử đăng ký với thông tin không hợp lệ
def test_invalid_register(driver):
    driver.get("http://localhost/opencartsite//")
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
    driver.find_element(By.ID, "input-firstname").send_keys("Van Phu")
    # Nhập Last Name vào trường nhập liệu, ở đây là "Tung"
    driver.find_element(By.ID, "input-lastname").send_keys("Tung")
    # Tạo email ngẫu nhiên
    # Nhập email vào trường nhập liệu
    random_email = f"DCT121C5user_{uuid.uuid4().hex[:8]}@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys(random_email)
    # Nhập Password không hợp lệ (thỏa 4-20 kí tự) vào trường nhập liệu, ở đây là "123"
    driver.find_element(By.ID, "input-password").send_keys("123")
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
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-password").text
    assert "Password must be between 4 and 20 characters!" in error_message

# TC03: Kiểm thử đăng ký với thông tin để trống
def test_register_with_empty_informatio(driver):
    driver.get("http://localhost/opencartsite//")
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
    # Để trống First Name
    driver.find_element(By.ID, "input-firstname").clear()
    # Để trống Last Name
    driver.find_element(By.ID, "input-lastname").clear()
    # Để trống địa chỉ email
    driver.find_element(By.ID, "input-email").clear()
    # Để trống password
    driver.find_element(By.ID, "input-password").clear()
    # Nhấp vào phần tử "agree"
    # agree_checkbox = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "//input[@type='checkbox' and @name='agree' and @value='1']"))
    # )
    # # Cuộn đến phần tử để đảm bảo nó hiện trong khung nhìn
    # driver.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)
    # time.sleep(1)  # Thêm một chút thời gian chờ để cuộn hoàn tất
    # agree_checkbox.click()
    # Chờ và nhấp vào nút "Continue"
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Continue']"))
    )
    # Cuộn đến vị trí của nút "Continue" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    continue_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-firstname").text
    assert "First Name must be between 1 and 32 characters!" in error_message
    error_message = driver.find_element(By.ID, "error-lastname").text
    assert "Last Name must be between 1 and 32 characters!" in error_message
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-password").text
    assert "Password must be between 4 and 20 characters!" in error_message
    # Chờ và lấy thông báo lỗi từ thẻ có id "alert"
    try:
        alert_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='alert']"))
        )
        error_message = alert_element.text
    except:
        error_message = ""
    # Kiểm tra nội dung thông báo lỗi
    assert "You must agree to the Privacy Policy" in error_message

# TC04: Kiểm thử đăng ký với email đã tồn tại
def test_register_with_email_already_exists(driver):
    driver.get("http://localhost/opencartsite//")
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
    driver.find_element(By.ID, "input-firstname").send_keys("Van Phu")
    # Nhập Last Name vào trường nhập liệu, ở đây là "Tung"
    driver.find_element(By.ID, "input-lastname").send_keys("Tung")
    # Nhập email đã tồn tại vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gmail.com")
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
    # Chờ và lấy thông báo lỗi từ thẻ có id "alert"
    try:
        alert_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='alert']"))
        )
        error_message = alert_element.text
    except:
        error_message = ""
    # Kiểm tra nội dung thông báo lỗi
    assert "E-Mail Address is already registered!" in error_message

# TC05: Kiểm thử đăng ký nếu không chấp nhận chính sách bảo mật
def test_register_if_privacy_policy_is_not_accepted(driver):
    driver.get("http://localhost/opencartsite//")
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
    driver.find_element(By.ID, "input-firstname").send_keys("Van Phu")
    # Nhập Last Name vào trường nhập liệu, ở đây là "Tung"
    driver.find_element(By.ID, "input-lastname").send_keys("Tung")
    # Tạo email ngẫu nhiên
    # Nhập email vào trường nhập liệu
    random_email = f"DCT121C5user_{uuid.uuid4().hex[:8]}@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys(random_email)
    # Nhập Password vào trường nhập liệu, ở đây là "12345"
    driver.find_element(By.ID, "input-password").send_keys("12345")
    # Nhấp vào phần tử "agree"
    # agree_checkbox = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "//input[@type='checkbox' and @name='agree' and @value='1']"))
    # )
    # # Cuộn đến phần tử để đảm bảo nó hiện trong khung nhìn
    # driver.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)
    # time.sleep(1)  # Thêm một chút thời gian chờ để cuộn hoàn tất
    # agree_checkbox.click()
    # Chờ và nhấp vào nút "Continue"
    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Continue']"))
    )
    # Cuộn đến vị trí của nút "Continue" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    continue_button.click()
    time.sleep(3)
    # Chờ và lấy thông báo lỗi từ thẻ có id "alert"
    try:
        alert_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='alert']"))
        )
        error_message = alert_element.text
    except:
        error_message = ""
    # Kiểm tra nội dung thông báo lỗi
    assert "You must agree to the Privacy Policy" in error_message


# Kiểm thử chức năng ĐĂNG NHẬP
# TC06: Kiểm thử đăng nhập với thông tin hợp lệ
def test_valid_login(driver):
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
    assert "http://localhost/opencartsite/index.php?route=account/login&language=en-gb" in driver.current_url
    # Nhập email vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gmail.com")
    # Nhập password vào trường nhập liệu, ở đây là "12345"
    driver.find_element(By.ID, "input-password").send_keys("12345")
    # Bấm nút Login
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']").click()
    time.sleep(3)
    assert "http://localhost/opencartsite/index.php?route=account/account&language=en-gb" in driver.current_url

# TC07: Kiểm thử đăng nhập với thông tin không hợp lệ
# (mật khẩu không hợp lệ - nằm ngoài trường 4-20 kí tự)
def test_invalid_login(driver):
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
    assert "http://localhost/opencartsite/index.php?route=account/login&language=en-gb" in driver.current_url
    # Nhập email vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gmail.com")
    # Nhập password vào trường nhập liệu, ở đây là "123" (mật khẩu không hợp lệ)
    driver.find_element(By.ID, "input-password").send_keys("123")
    # Bấm nút Login
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']").click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Chờ và lấy thông báo lỗi từ thẻ có id "alert"
    try:
        alert_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='alert']"))
        )
        error_message = alert_element.text
    except:
        error_message = ""
    # Kiểm tra tính chính xác của nội dung thông báo lỗi
    assert "No match for E-Mail Address and/or Password" in error_message

# TC08: Kiểm thử đăng nhập với thông tin để trống
def test_login_with_empty_information(driver):
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
    # Để trống email
    driver.find_element(By.ID, "input-email").clear()
    # Để trống mật khẩu
    driver.find_element(By.ID, "input-password").clear()
    # Bấm nút Login
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']").click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Chờ và lấy thông báo lỗi từ thẻ có id "alert"
    try:
        alert_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='alert']"))
        )
        error_message = alert_element.text
    except:
        error_message = ""
    # Kiểm tra nội dung thông báo lỗi
    assert "No match for E-Mail Address and/or Password." in error_message


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


# Kiểm thử chức năng NỘP BIỂU MẪU
# TC10: Kiểm thử nộp biểu mẫu liên hệ với thông tin hợp lệ
def test_valid_form_submission_contact_us(driver):
    driver.get("http://localhost/opencartsite//")
    # Chờ và nhấp vào "fa-solid fa-phone"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/opencartsite/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Nhập Your Name vào trường nhập liệu, ở đây là "Van Phu Tung"
    driver.find_element(By.ID, "input-name").send_keys("Van Phu Tung")
    # Nhập email vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gmail.com")
    # Nhập Enquiry vào trường nhập liệu, ở đây là "Your product is very good!"
    driver.find_element(By.ID, "input-enquiry").send_keys("Your product is very good!")
    # Nhấp vào nút "Submit"
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    submit_button.click()
    time.sleep(3)
    assert "http://localhost/opencartsite/index.php?route=information/contact.success&language=en-gb" in driver.current_url

# TC11: Kiểm thử nộp biểu mẫu liên hệ với thông tin không hợp lệ
def test_invalid_form_submission_contact_us(driver):
    driver.get("http://localhost/opencartsite//")
    # Chờ và nhấp vào "fa-solid fa-phone"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/opencartsite/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Nhập Your Name vào trường nhập liệu, ở đây là "VanTung"
    driver.find_element(By.ID, "input-name").send_keys("VanTung")
    # Nhập email không hợp lệ vào trường nhập liệu, ở đây là "DCT121C5user1@gma*il.com"
    driver.find_element(By.ID, "input-email").send_keys("DCT121C5user1@gma*il.com")
    # Nhập Enquiry không hợp lệ (nằm ngoài 10-3000 ký tự) vào trường nhập liệu, ở đây là "alo123@"
    driver.find_element(By.ID, "input-enquiry").send_keys("alo123@")
    # Nhấp vào nút "Submit"
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    submit_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-enquiry").text
    assert "Enquiry must be between 10 and 3000 characters!" in error_message

# TC12: Kiểm thử nộp biểu mẫu liên hệ với thông tin để trống
def test_form_submission_contact_us_with_empty_informationform(driver):
    driver.get("http://localhost/opencartsite//")
    # Chờ và nhấp vào "fa-solid fa-phone"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/opencartsite/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Để trống Your Name
    driver.find_element(By.ID, "input-name").clear()
    # Để trống địa chỉ email
    driver.find_element(By.ID, "input-email").clear()
    # Để trống Enquiry
    driver.find_element(By.ID, "input-enquiry").clear()
    # Nhấp vào nút "Submit"
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    submit_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-name").text
    assert "Name must be between 3 and 32 characters!" in error_message
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-enquiry").text
    assert "Enquiry must be between 10 and 3000 characters!" in error_message


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
    # Xác minh URL điều hướng tới trang Show All Desktops
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
    # Xác minh URL điều hướng tới trang Macs
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
    # Xác minh URL điều hướng tới trang Windows
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
    # Xác minh URL điều hướng tới trang Show All Laptops & Notebooks
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

# Kiểm thử chức năng THÊM VÀO GIỎ HÀNG
# TC18: Kiểm thử thêm 1 sản phẩm vào giỏ hàng
def test_add_to_cart_1_product(driver):
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

# TC20: Kiểm thử thêm nhiều sản phẩm khác nhau vào giỏ hàng
def test_add_to_cart_many_products(driver):
    driver.get("http://localhost/opencartsite//")
    ''' Thêm sản phẩm MacBook'''
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
    # Nhập vào thanh số lượng ngẫu nhiên (từ 1 tới 10)
    quantity_input.send_keys(str(random.randint(1, 10)))
    # Tìm nút "Add to Cart" dựa trên các thuộc tính của nút
    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_to_cart_button.click()
    time.sleep(2)
    ''' Thêm sản phẩm Palm Treo Pro'''
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
    # Tìm hình ảnh của Palm Treo Pro bằng thuộc tính 'alt' hoặc 'title'
    palmtreopro_image = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='Palm Treo Pro' and @title='Palm Treo Pro']")
        )
    )
    # Cuộn đến phần tử hình ảnh Palm Treo Pro để đảm bảo nó hiện trong khung nhìn
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

# Kiểm thử chức năng THANH TOÁN
# TC21: Kiểm thử thanh toán với thông tin hợp lệ
def test_valid_checkout(driver):
    driver.get("http://localhost/opencartsite//")
    ''' Bước chọn sản phẩm '''
    # Thêm sản phẩm Palm Treo Pro
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
    # Tìm hình ảnh của Palm Treo Pro bằng thuộc tính 'alt' hoặc 'title'
    palmtreopro_image = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@alt='Palm Treo Pro' and @title='Palm Treo Pro']")
        )
    )
    # Cuộn đến phần tử hình ảnh Palm Treo Pro để đảm bảo nó hiện trong khung nhìn
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

# TC25: Kiểm thử tìm kiếm với đầu vào để trống
def test_search_no_information(driver):
    driver.get("http://localhost/opencartsite/")
    time.sleep(2)
    # Để trống ô tìm kiếm
    driver.find_element(By.NAME, "search").clear()
    # Click vào nút tìm kiếm
    driver.find_element(By.CLASS_NAME, "btn-light").click()
    time.sleep(2)
    # Kiểm tra từ khóa không hợp lệ trong kết quả tìm kiếm
    assert "" in driver.page_source
    # Kiểm tra thông báo "There is no product that matches the search criteria."
    assert "There is no product that matches the search criteria." in driver.page_source
