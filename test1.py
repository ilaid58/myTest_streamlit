import streamlit as st

st.write('welcome to my streamlit app')
a = st.text_input('enter n1 ')
b = st.text_input('enter n2 ')

if st.button('valid'):
	a = int(a.title())
	b = int(b.title())
	st.write(a, '+', b, '=', a+b)

upload_file = st.file_uploader('upload a file')
data = upload_file.read()
name = upload_file.name
st.write('filename', name)
st.write(data)
