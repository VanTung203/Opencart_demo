# Hướng Dẫn Chạy Code Kiểm Thử Python với Selenium trên PyCharm

## Cài Đặt Môi Trường

1. **Ngôn ngữ lập trình:**
   - Python.

2. **IDE:**
   - PyCharm.

3. **Cài đặt Selenium WebDriver trong PyCharm:**
   - Mở PyCharm và cài đặt Selenium bằng cách sử dụng `pip`:
     ```bash
     pip install selenium
     ```

4. **Trình duyệt:**
   - Google Chrome.

5. **Cài đặt XAMPP:**
   - Tải và cài đặt XAMPP từ [Trang chủ XAMPP](https://www.apachefriends.org/index.html).
   - Mở XAMPP Control Panel và khởi động "Apache" và "MySQL".

## Cách Chạy Mã Kiểm Thử

### 1. Mở PyCharm
   - Mở PyCharm và mở dự án chứa mã kiểm thử.

### 2. Khởi động XAMPP
   - Đảm bảo rằng XAMPP đã được cài đặt và đang chạy. Khởi động "Apache" và "MySQL" trong XAMPP Control Panel.

### 3. Cài đặt Các Module Cần Thiết
   - Đảm bảo rằng đã cài đặt các module cần thiết như `pytest`, `selenium`, và các module liên quan khác:
     ```bash
     pip install pytest selenium
     ```

## Cách Thực Thi Mã Kiểm Thử

### 1. Chạy Kiểm Thử Theo Lô (Batch Execution)
   - Lưu tất cả mã kiểm thử vào một tệp.
   - Nhấp chuột phải vào tệp chứa các bài kiểm thử, sau đó chọn "Run Tests" (Chạy các bài kiểm thử).
   
### 2. Chạy Kiểm Thử Từng Phần (Individual Execution)
   - Lưu tất cả mã kiểm thử vào một tệp.
   - Một biểu tượng hình tam giác sẽ xuất hiện bên cạnh tên của mỗi hàm kiểm thử.
   - Nhấp vào biểu tượng tam giác của hàm kiểm thử muốn chạy.
   - **Hoặc**
     - Lưu từng hàm kiểm thử vào các tệp riêng biệt và chạy từng hàm kiểm thử riêng lẻ.
     - Điều này có thể giúp kiểm thử từng phần độc lập, đồng thời dễ quan sát cấu trúc hơn.

Sau khi hoàn tất, ta sẽ thấy kết quả kiểm thử trong bảng điều khiển của PyCharm.
