import streamlit as st

st.write('welcome to my streamlit app')
a = st.text_input('enter n1 ')
b = st.text_input('enter n2 ')

if st.button('valid'):
	a = int(a.title())
	b = int(a.title())
	st.write(a, '+', b, '=', a+b)

