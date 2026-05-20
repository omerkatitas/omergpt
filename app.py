import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="ÖmerGPT",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ÖmerGPT")
st.caption("Zekice cevap veren yapay zekâ asistanı")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

soru = st.chat_input("ÖmerGPT'ye bir şey sor...")

if soru:
    st.session_state.messages.append({"role": "user", "content": soru})

    with st.chat_message("user"):
        st.write(soru)

    with st.chat_message("assistant"):
        with st.spinner("ÖmerGPT düşünüyor..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                instructions="""
                Senin adın ÖmerGPT.
                Türkçe konuşan, zeki, açıklayıcı ve yardımsever bir asistansın.
                Eğitim, matematik, teknoloji, kodlama ve günlük sorularda destek olursun.
                Cevapların anlaşılır, düzenli ve gereksiz uzun olmayan biçimde olmalı.
                """,
                input=soru
            )

            cevap = response.output_text
            st.write(cevap)

    st.session_state.messages.append({"role": "assistant", "content": cevap})
