import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import hashlib
import os
from pathlib import Path
import time
import base64
import time
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import streamlit.components.v1 as components
from src.auth.auth import login, register
from src.schedule.schedule_display import display_schedule  # Import display_schedule
from src.pomodoro.pomodoro_display import display_pomodoro
from src.Background import set_background
from src.Background import change_background
from src.Introduction import introduction
from src.Instruction_of_use import instruction_of_use

def main():
    # Thiết lập cấu hình trang
    st.set_page_config(
    page_title="Quản Lý Thời Gian và Lịch Trình",
    page_icon="🕒",
    layout="wide",
    ) 
    set_background()
    ###################################################################################################
    df = px.data.iris()
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return encoded
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, 'assets')
    img_path = os.path.join(assets_dir, '7.png')
    img1_path = os.path.join(assets_dir, 'Background.png')
    img = get_img_as_base64(img_path)
    img1 = get_img_as_base64(img1_path)
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{img1}");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    # CSS tùy chỉnh để tạo hiệu ứng hover với animation cho sidebar
    st.markdown("""
    <style>
    /* Nền của sidebar */
    .css-1aumxhk {
        background-color: #0d0c0c;
    }   
    /* Tạo animation khi hover Sidebar */
    .stSidebar .stSelectbox > div:hover {
        background-color: #E8E8E8;
        color: #c41414;
        transform: scale(1.1); /* Phóng to nhẹ */
        transition: transform 0.2s ease, background-color 0.05s ease; /* Animation khi hover */
    }
    .stSelectbox > div:hover {
        background-color: #E8E8E8;
        transform: scale(1.1); /* Phóng to nhẹ */
        transition: transform 0.2s ease, background-color 0.2s ease; /* Animation khi hover */
    }
    /* Tạo hiệu ứng chuyển động nhấp nháy */
    .stSidebar .stSelectbox > div:hover {
        animation: glow s ease-in-out infinite alternate; /* Hiệu ứng chuyển động nhấp nháy */
    }
    .stSelectbox > div:hover {
        animation: glow 1s ease-in-out infinite alternate; /* Hiệu ứng chuyển động nhấp nháy */
    }
    /* Tuỳ chỉnh màu tiêu đề SlectBox */
    .stSidebar .stSelectbox label {
        font-family: 'Arial', sans-serif; 
        font-size: 100px;
        color: #ffcc00; /* Màu chữ của tiêu đề */
        font-weight: bold;
        margin-bottom: 0px;    /* Khoảng cách dưới */
        display: inline-block;
    }
    .stSelectbox label {
        font-family: 'Arial', sans-serif; 
        font-size: 50px;
        color: #ffcc00; /* Màu chữ của tiêu đề */
        font-weight: bold;
    }
    
    /* Tùy chỉnh phông chữ và hiệu ứng của các mục chọn */
    .stSidebar .stSelectbox > div {
        background-color: #1c1c1e; /* Màu nền của selectbox */
        color: white; /* Màu chữ của selectbox */
        font-size: 16px;
        border-radius: 10px;
        padding: 5px;
        transition: all 0.3s ease; /* Thời gian chuyển đổi chung */
    }
    .stSelectbox > div {
        background-color: #1c1c1e; /* Màu nền của selectbox */
        color: white; /* Màu chữ của selectbox */
        font-size: 16px;
        border-radius: 10px;
        padding: 5px;
        transition: all 0.3s ease; /* Thời gian chuyển đổi chung */
    }
    
    /* Keyframes cho hiệu ứng glow */
    @keyframes glow {
        from {
            box-shadow: 0 0 5px #ff6600, 0 0 10px #ff6600;
        }
        to {
            box-shadow: 0 0 20px #ffcc00, 0 0 30px #ffcc00;
        }
    }
    .custom-select select {
        display: none; /* Ẩn phần tử select gốc */
    }
    .hover-3d {
    transition: transform 0.2s ease-in-out;
    }
    .hover-3d:hover {
    transform: rotateX(15deg) rotateY(15deg) scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)
    # Đổi màu toàn bộ Dropdown của Các SelectBox trong ứng dụng
    st.markdown("""
        <style>
    /* Main container */
    [data-baseweb="select"] {
        background-color: #1E1E1E;
    } 
    /* Dropdown menu container */
    [data-baseweb="popover"] {
        background-color: #1E1E1E !important;
    }   
    /* Menu container */
    [data-baseweb="menu"] {
        background-color: #1E1E1E !important;
        padding: 0 !important;  /* Remove padding */
    }   
    /* Each option item */
    [data-baseweb="menu"] div[role="option"] {
        background-color: #1E1E1E !important;
        color: white !important;
        padding: 8px 16px !important;  /* Add padding to option itself */
        width: 100% !important;  /* Full width */
        margin: 0 !important;  /* Remove margin */
    }   
    /* Hover effect for options */
    [data-baseweb="menu"] div[role="option"]:hover {
        background-color: #06775F !important;
        color: white !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 8px 16px !important;
    }    
    /* Selected option */
    [role="option"][aria-selected="true"] {
        background-color: #06775F !important;
        width: 100% !important;
    }    
    /* Override any default hover styles */
    [data-baseweb="menu"] div[role="option"][data-highlighted="true"] {
        background-color: #06775F !important;
        width: 100% !important;
    }   
    /* Remove any gaps or spaces */
    [data-baseweb="menu"] > div {
        padding: 0 !important;
        margin: 0 !important;
    }    
    /* Ensure the list takes full width */
    [data-baseweb="list"] {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(page_bg_img, unsafe_allow_html=True)
    def set_button_hover_style():
        st.markdown("""
        <style>
        /* Hiệu ứng hover cho tất cả các nút trong ứng dụng */
        button:hover {
            background-color: #F6F5F4; /* Màu nền khi hover */
            color: white; /* Màu chữ khi hover */
            transform: scale(1.15); /* Phóng to nhẹ */
            transition: transform 0.5s ease, background-color 0.5s ease; /* Animation khi hover */
            border-radius: 10px; /* Bo góc cho nút */
            box-shadow: 0 0 10px rgba(255, 102, 0, 0.5); /* Hiệu ứng bóng */
            animation: glow 1s ease-in-out infinite alternate;
        }
        /* Hiệu ứng khi nhấn vào nút */
        .stButton>button:active {
            transform: scale(0.98); /* Thu nhỏ nhẹ khi nhấn */
         box-shadow: 0px 2px 4px rgba(255, 102, 0, 0.2); /* Đổ bóng nhẹ hơn khi nhấn */
    }
        .bounce-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #06775F;
    color: white;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    transition: transform 0.2s ease-in-out;
    }
        .bounce-button:hover {
    animation: bounce 1s infinite;
    }

    @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
    }
    40% {
    transform: translateY(-10px);
    }
    60% {
    transform: translateY(-5px);
    }
} 
        </style>
    """, unsafe_allow_html=True)
    # Cấu hình particles.js tùy chỉnh cho ứng dụng học tập
    particles_js_config = '''
{
  "particles": {
    "number": {
      "value": 100,
      "density": {
        "enable": true,
        "value_area": 800
      }
    },
    "shape": {
      "type": "char",
      "character": {
        "value": ["A", "B", "C", "1", "2", "3", "α", "β", "γ"],
        "font": "Verdana",
        "style": "",
        "weight": "bold",
        "fill": true
      }
    },
    "color": {
      "value": "#00aaff"
    },
    "opacity": {
      "value": 0.8
    },
    "size": {
      "value": 16,
      "random": true
    },
    "move": {
      "enable": true,
      "speed": 2,
      "direction": "none",
      "out_mode": "out"
    }
  },
  "interactivity": {
    "events": {
      "onhover": {
        "enable": true,
        "mode": "repulse"
      },
      "onclick": {
        "enable": false
      }
    },
    "modes": {
      "repulse": {
        "distance": 100
      }
    }
  },
  "retina_detect": true
}
'''
    # Gọi hàm này ở đầu ứng dụng để áp dụng hiệu ứng
    set_button_hover_style()
    ###################################################################################################
    # Tên ứng dụng
    st.title("Ứng Dụng Quản Lý Thời Gian và Lịch Trình 🤝")
    # Kiểm tra trạng thái đăng nhập trong session
    if 'is_logged_in' not in st.session_state:
        st.session_state['is_logged_in'] = False
        st.session_state['username'] = ''
    # Menu lựa chọn giữa Đăng nhập và Đăng ký
    menu = ["Đăng Nhập", "Đăng Ký"]
    option = st.sidebar.selectbox("User Account", menu)
    if not st.session_state['is_logged_in']:
        if option == "Đăng Nhập":
            if login():
                st.session_state.is_logged_in = True
        elif option == "Đăng Ký":
            register()
    else:
        # Hiển thị menu chính khi đã đăng nhập
        st.sidebar.success(f"Đã đăng nhập: {st.session_state['username']}")
        # Tạo menu chính
        main_menu = st.sidebar.selectbox(
            "Menu",
            ["Giới Thiệu Ứng Dụng","Hướng dẫn sử dụng", "Công Cụ Học Tập","Đổi ảnh nền"]
    )
        if main_menu == "Giới Thiệu Ứng Dụng":
            st.balloons()
            st.snow()
            introduction()
        elif main_menu == "Đổi ảnh nền":
            st.balloons()
            change_background()
        elif main_menu == "Hướng dẫn sử dụng":
            st.balloons()
            instruction_of_use()
        elif main_menu == "Công Cụ Học Tập":
            # Tính năng bổ sung
            sub_menu = st.sidebar.selectbox(
                "Các Công Cụ Chính",
                ["Phương Pháp Pomodoro", "Quản lý Thời gian biểu", "Thiết Lập Tài Khoản"]
            )
            # Nội dung cho các tính năng bổ sung
            if sub_menu == "Phương Pháp Pomodoro":
                st.snow()
                display_pomodoro()
            elif sub_menu == "Quản lý Thời gian biểu":
                st.snow()
                st.header("Quản lý thời gian học tập thông minh")
                if not st.session_state.is_logged_in:
                    st.warning("Bạn cần phải đăng nhập để truy cập vào tính năng này.")
                else:
                    # Gọi hàm hiển thị lịch trình từ file khác
                    display_schedule()    
        elif sub_menu == "Thiết Lập Tài Khoản":
            st.balloons()
            st.header("⚙️ Thiết Lập Tài Khoản")
            st.write("...Thiết lập tài khoản...")
        if st.sidebar.button("Đăng xuất"):
            st.snow()
            st.balloons()
            st.session_state['is_logged_in'] = False
            st.session_state['username'] = ''
            st.toast('Đăng xuất thành công')
            st.rerun()
if __name__ == "__main__":
    main() 