import streamlit as st
from streamlit_lottie import st_lottie
import requests
# Hàm để tải nội dung Lottie từ URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Hàm để hiển thị nội dung "Hướng dẫn sử dụng"
def instruction_of_use():
    st.balloons()
    st.header("🎉Hướng Dẫn Sử Dụng Ứng Dụng Quản Lý Thời Gian và Lịch Trình")
    # URL của hoạt hình Lottie thứ nhất
    lottie_url1 = "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json"
    lottie_json1 = load_lottieurl(lottie_url1)
    # Hiển thị hoạt hình Lottie thứ nhất
    st_lottie(
        lottie_json1,
        height=300,
        key="education_lottie",
    )
    # URL của hoạt hình Lottie thứ hai (nếu cần)
    lottie_url2 = "https://assets2.lottiefiles.com/packages/lf20_x62chJ.json"
    lottie_json2 = load_lottieurl(lottie_url2)
    # Hiển thị hoạt hình Lottie thứ hai
    st_lottie(
        lottie_json2,
        height=300,
        key="lottie",
    )
    # Hiển thị nội dung hướng dẫn sử dụng
    st.markdown("""
    Người dùng có thể tùy chọn kích hoạt phương pháp học tập Pomodoro. Khi bắt đầu, nhấn nút "Start" để kích hoạt đồng hồ đếm ngược cho phiên làm việc kéo dài từ 25-30 phút. Sau khi kết thúc một phiên làm việc, hệ thống sẽ tự động thông báo và bắt đầu thời gian nghỉ giải lao ngắn kéo dài 5 phút. Chu kỳ này sẽ lặp lại cho đến khi hoàn thành công việc. Sau 4 lần nghỉ giải lao ngắn, người dùng sẽ được nhắc nghỉ dài hơn, kéo dài từ 10-15 phút.

    Ngoài ra, ứng dụng tích hợp đồng hồ hiển thị thời gian, cung cấp một số câu truyền động lực, và đặc biệt có tùy chọn phát nhạc lofi không lời giúp tạo không gian làm việc tập trung. Người dùng có thể bật hoặc tắt nhạc lofi tùy thích trong quá trình sử dụng.
    """)
