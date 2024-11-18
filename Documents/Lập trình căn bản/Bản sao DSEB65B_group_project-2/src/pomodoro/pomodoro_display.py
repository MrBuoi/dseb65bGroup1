import streamlit as st
import time
from pathlib import Path
def display_pomodoro():
    # Main title
    st.write("""
    # The Pomodoro App
    Let's do some focus work with this app.
    """)
    # Timer countdown
    t1 = 1500  # 25 minutes for focus
    t2 = 300   # 5 minutes for break
    # Center the "Start" button using columns
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        button_clicked = st.button("Start")
    if button_clicked:
        with st.empty():
            while t1:
                mins, secs = divmod(t1, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"⏳ {timer}")
                time.sleep(0.01)
                t1 -= 1
            st.success("🔔 25 minutes is over! Time for a break!")
        st.balloons()
        with st.empty():
            while t2:
                mins2, secs2 = divmod(t2, 60)
                timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
                st.header(f"⏳ {timer2}")
                time.sleep(0.01)
                t2 -= 1
            st.error("⏰ 5 minute break is over!")
    # Music selection
    st.markdown("### 🎵 Choose background music")
    # Lấy đường dẫn của file hiện tại
    #current_dir = Path(__file__).parent
    # Xây dựng đường dẫn đến thư mục Assets
    #assets_dir = current_dir.parent.parent / 'assets'
    # Xây dựng đường dẫn đến các file nhạc
    #music_files = {
        #"Lofi Beats": assets_dir / 'lofi.mp3',
        #"Classical Music": assets_dir / 'classic.mp3',
        #"Healing Music": assets_dir / 'healing.mp3',
        #"Piano Music": assets_dir / 'piano.mp3',
        #"Electronic Music": assets_dir / 'edm.mp3'
    #}
    # Dropdown for selecting music
    #selected_music = st.selectbox("Select a music track:", list(music_files.keys()))
    # Load selected audio file
    #audio_file_path = music_files[selected_music]
    #audio_file = open(audio_file_path, "rb")
    #audio_bytes = audio_file.read()
    #if 'is_playing' not in st.session_state:
        #st.session_state.is_playing = False
    # Center the "Play/Pause Music" button
    col4, col5, col6 = st.columns([1, 1, 1])
    with col5:
        if st.button('Play/Pause Music'):
            st.session_state.is_playing = not st.session_state.is_playing
    # Play or pause audio based on button state
    #if st.session_state.is_playing:
        #st.audio(audio_bytes, format="audio/mp3")
    # Additional information
    st.write("""
    # An online Pomodoro Timer to boost your productivity
    """)
    st.markdown("**_What is Pomofocus?_**")
    st.write("""Pomofocus is a customizable pomodoro timer that works on 
            desktop & mobile browser. The aim of this app is to help 
            you focus on any task you are working on, such as study, 
            writing, or coding. This app is inspired by Pomodoro 
            Technique which is a time management method developed 
            by Francesco Cirillo.""")
    st.markdown("**_What is Pomodoro Technique?_**")
    st.write("""The Pomodoro Technique is created by Francesco Cirillo for 
            a more productive way to work and study. The technique uses
            a timer to break down work into intervals, traditionally 
            25 minutes in length, separated by short breaks. Each 
            interval is known as a pomodoro, from the Italian word for 
            'tomato', after the tomato-shaped kitchen timer that Cirillo 
            used as a university student. - Wikipedia""")
    st.markdown("**_How to use the Pomodoro Timer?_**")
    st.write("""1. Add tasks to work on today""")
    st.write("2. Set estimate pomodoros (1 = 25min of work) for each tasks")
    st.write("3. Select a task to work on")
    st.write("4. Start timer and focus on the task for 25 minutes")
    st.write("5. Take a break for 5 minutes when the alarm ring")
    st.write("6. Iterate 3-5 until you finish the tasks")
