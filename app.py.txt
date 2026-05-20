import streamlit as st

st.title("🤖 ÖmerGPT")

soru = st.chat_input("Bir şey sor...")

if soru:
    st.chat_message("user").write(soru)

    cevap = f"Sen şunu sordun: {soru}"

    st.chat_message("assistant").write(cevap)