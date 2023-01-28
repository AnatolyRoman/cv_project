import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
    page_title="YOLO",
    page_icon="🤓",
)

def get_main_bar():
    
    # set title and description 
    header = st.columns([2,1])
    with header[0]:
        st.markdown('''<h1 style="text-align: left; font-family: 'Gill Sans'; color: #D8D8D8"
            ></h1><h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00"
            >YOLO</h1>''', 
            unsafe_allow_html=True)
    with header[0]:
        st.markdown('''<h1 style="text-align: left; font-family: 'Gill Sans'; color: #D8D8D8"
            >You Only Look Once</h1><h1 style="text-align: left; font-family: 'Gill Sans'; color: #FF2A00"
            ></h1>''', 
            unsafe_allow_html=True)
    with header[1]:
        for num in range(7):
            st.markdown('')
        st.markdown('''<h3 style="text-align: right; font-family: 'Gill Sans'; color: #FF2A00"
            >by Sirazhudin, Anatoly, Semyon</h3>''', 
            unsafe_allow_html=True)
    
    for num in range(2):
        st.markdown(" ")
    st.markdown('''<p style="text-align: left; font-family: 'Gill Sans'; font-size: 20px; color: #D8D8D8">
            YOLO (You Only Look Once) — архитектура нейронных сетей, предназначенная для детекции объектов на изображении. Отличительной особенностью YOLO является подход к решению задачи детекции.</p>''', 
            unsafe_allow_html=True)

get_main_bar()


st.video('YOLOvideo.MOV')


