import streamlit as st
#import cv2
st.write('welcome to my streamlit app')
a = st.text_input('enter n1 ')
b = st.text_input('enter n2 ')

if st.button('valid'):
	a = int(a.title())
	b = int(b.title())
	st.write(a, '+', b, '=', a+b)

upload_file = st.file_uploader('upload a file')
#st.write(st.__dict__)
#data = upload_file.read()
#name = upload_file.name
#st.write('filename', name)
#st.write(data)
#cv2.imwrite()
color = st.color_picker('pick a color', '#00f900')
st.write('the current color ',color)
st.slider('slider ', 1.0, 2.0, 10.0)

with open("flower.txt", "w+") as file:
	file.write('salut')
	st.download_button(
	label="Download image",
	data=file,
	file_name="flower.txt",
	mime="image/png")
opt = st.selectbox('select option', ['a', 'b', 'c'])
st.write(opt)

