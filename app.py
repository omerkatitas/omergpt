import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="ÖmerGPT", page_icon="🤖")

st.title("🤖 ÖmerGPT")
st.write("Merhaba 😄 Ben ÖmerGPT")

client = InferenceClient(api_key=st.secrets["HF_TOKEN"])

if "chat" not in st.session_state:
    st.session_state.chat = []

for mesaj in st.session_state.chat:
    with st.chat_message(mesaj["role"]):
        st.write(mesaj["content"])

soru = st.chat_input("Bir şey sor...")

if soru:
    st.session_state.chat.append({"role": "user", "content": soru})

    with st.chat_message("user"):
        st.write(soru)

    with st.chat_message("assistant"):
        with st.spinner("ÖmerGPT düşünüyor..."):
            try:
                response = client.chat.completions.create(
                    model="HuggingFaceH4/zephyr-7b-beta",
                    messages=[
                        {
                            "role": "system",
                            "content": "Senin adın ÖmerGPT. Türkçe konuşan, yardımsever ve açıklayıcı bir yapay zekâ asistanısın."
                        },
                        *st.session_state.chat
                    ],
                    max_tokens=500
                )

                yanit = response.choices[0].message.content
                st.write(yanit)

                st.session_state.chat.append({
                    "role": "assistant",
                    "content": yanit
                })

            except Exception as e:
                st.error("Model cevap veremedi. Hata:")
                st.code(str(e))
