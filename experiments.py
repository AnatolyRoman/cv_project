import streamlit as st
import pandas as pd 
import time as ts
from datetime import time


st.markdown("""" 
<style>
.css-d1b1kd.edgvbvh6
{
    visibility:hidden;
}
.css-1v8iw7l.eknhn3m4;
{
    visibility: hidden;
}
</style>
""")


tabel = pd.DataFrame({'Column1': [1, 2, 3, 4, 5, 6, 7], 'Column2': [11, 12, 13, 14, 15, 16, 17]})

st.title('Uploading Files')
st.markdown('---')

def converter(value):
    m, s, mm = value.split(':')
    t_s = int(m) * 60 + int(s) + int(mm)/  1000
    return t_s
images = st.file_uploader('Please upload an Image', type = ['png', 'jpg'], accept_multiple_files = True)
if images is not None:
    for image in images:
        st.image(image)


st.slider('This is a Slider', min_value = 50, max_value = 150, value = 70)

val = st.time_input('Set timer', value = time(0, 0, 0))
if str(val) == '00:00:00':
    st.write('Please sent timer')
else:
    sec = converter(str(val))
    bar = st.progress(0)
    per = sec/100
    for i in range(10):
        bar.progress((i + 1))
        ts.sleep(per)

















