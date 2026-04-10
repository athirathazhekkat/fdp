import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit application.")
st.header("Features")
st.subheader("Easy to Use")
st.markdown("- Streamlit allows you to create web apps with just a few lines of code.")
st.markdown("<h1>Im HTML Code</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='color:green;'>Im HTML & CSS Code</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='color:blue; font-size: 100px;'>Im HTML & CSS Code</h1>", unsafe_allow_html=True)
