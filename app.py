import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="ÖmerGPT",
    page_icon="🤖"
)

st.title("🤖 ÖmerGPT")
st.write("Merhaba 😄 Ben ÖmerGPT")

client = InferenceClient(
    provider="hf-inference",
    api_key=st.secrets["HF_TOKEN"]
)

if "chat" not in st.session_state:
    st.session_state.chat = []

for mesaj in st.session_state.chat:
    with st.chat_message(mesaj["role"]):
        st.write(mesaj["content"])

soru = st.chat_input("Bir şey sor...")

if soru:

    st.session_state.chat.append({
        "role": "user",
        "content": soru
    })

    with st.chat_message("user"):
        st.write(soru)

    with st.chat_message("assistant"):

        with st.spinner("ÖmerGPT düşünüyor..."):

            cevap = client.chat.completions.create(
                model="Qwen/Qwen2.5-7B-Instruct",
                messages=[
                    {
                        "role": "system",
                        "content": "Senin adın ÖmerGPT. Türkçe konuşan yardımsever bir asistansın."
                    },
                    *st.session_state.chat
                ],
                max_tokens=500
            )

            yanit = cevap.choices[0].message.content

            st.write(yanit)

    st.session_state.chat.append({
        "role": "assistant",
        "content": yanit
    })
