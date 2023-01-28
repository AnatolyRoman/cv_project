import streamlit as st
import pandas as pd 
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np


# tabel = pd.DataFrame({'Column1': [1, 2, 3, 4, 5, 6, 7], 'Column2': [11, 12, 13, 14, 15, 16, 17]})

# st.title('Uploading Files')
# st.markdown('---')

# def converter(value):
#     m, s, mm = value.split(':')
#     t_s = int(m) * 60 + int(s) + int(mm)/  1000
#     return t_s
# images = st.file_uploader('Please upload an Image', type = ['png', 'jpg'], accept_multiple_files = True)
# if images is not None:
#     for image in images:
#         st.image(image)
# val = st.time_input('Set timer', value = time(0, 0, 0))
# if str(val) == '00:00:00':
#     st.write('Please sent timer')
# else:
#     sec = converter(str(val))
#     print(sec)
#     bar = st.progress(0)
#     per = sec/100
#     progress_status = st.empty()
#     for i in range(100):
#         bar.progress((i + 1))
#         progress_status.write(str(i + 1) + ' %')
#         ts.sleep(per)


# st.markdown("<h1 style = 'text-align: center;'> User Registration</h1>", unsafe_allow_html = True)
# # form = st.form('Form 1')
# # form.text_input('First Name')
# # form.form_submit_button('Submit')
# with st.form('Form 2', clear_on_submit = False):
#     col1, col2 = st.columns(2)
#     f_name = col1.text_input('First Name')
#     l_name = col2.text_input('Last Name')
#     st.text_input('Email Address')
#     st.text_input('Password')
#     st.text_input('Confirm Password')
#     day, month, year = st.columns(3)
#     day.text_input('Day')
#     month.text_input('Month')
#     year.text_input('Year')
#     s_state = st.form_submit_button('Submit')
#     if s_state:
#         if f_name == '' and l_name == '':
#             st.warning('Please Fill above fields', icon = '🚨')
#         else:
#             st.success('Submit Successfully', icon = '✅')


# x = np.linspace(0, 10, 100)
# bar_x = np.array([1, 2, 3, 4, 5])
# opt = st.sidebar.radio('Select Any Graph', options = ('Line', 'Bar', 'H-bar'))
# if opt == 'Line':
#     st.markdown("<h1 style = 'text-align: center;'>Line Chart</h1>", unsafe_allow_html = True)
#     fig = plt.figure()
#     plt.style.use('https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle')
#     plt.plot(x, np.sin(x))
#     plt.plot(x, np.cos(x), '--')
#     st.write(fig)
# elif opt == 'Bar':
#     st.markdown("<h1 style = 'text-align: center;'>Bar Chart</h1>", unsafe_allow_html = True)
#     fig = plt.figure()
#     plt.style.use('https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle')
#     plt.bar(bar_x,bar_x * 10)
#     st.write(fig)
# else:
#     st.markdown("<h1 style = 'text-align: center;'>H-Bar Chart</h1>", unsafe_allow_html = True)
#     fig = plt.figure()
#     plt.style.use('https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle')
#     plt.barh(bar_x * 10, bar_x)
#     st.write(fig)

































