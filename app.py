import streamlit as st
from PIL import Image
from vqa_model import VQAModel
import os

st.set_page_config(page_title="GQA Visual Question Answering", layout="centered")
st.title("🚀 GQA Visual Question Answering")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
question = st.text_input("Ask a question about the image:")
voice_button = st.button("🎤 Ask with Voice")

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    model = VQAModel()

    if voice_button:
        with st.spinner("Listening for your question..."):
            q, a = model.ask_with_voice(image)
        if q:
            st.markdown(f"**You asked:** {q}")
        st.markdown(f"### 🌐 Answer: `{a}`")

    elif question:
        with st.spinner("Thinking..."):
            answer = model.predict(image, question)
        st.markdown(f"### 🌐 Answer: `{answer}`")
