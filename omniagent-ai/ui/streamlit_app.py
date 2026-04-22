import streamlit as st
import requests

st.title("OmniAgent AI")

user_input = st.text_input("Ask anything:")

if st.button("Send"):
    res = requests.post("http://localhost:8000/chat", json={"message": user_input})
    st.write(res.json())