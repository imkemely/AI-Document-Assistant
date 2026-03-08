import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

st.title("AI Document Assistant")

# initialize the Groq client once and store in session
if "client" not in st.session_state:
    st.session_state.client = Groq(api_key=api_key)

with st.sidebar:
    st.header("Setup")
    uploaded_file_ui = st.file_uploader("Upload your document", type=["pdf", "txt"])

    if uploaded_file_ui and "doc_text" not in st.session_state:
        with st.spinner("Uploading document..."):
            if uploaded_file_ui.type == "application/pdf":
                # extract text properly from PDF
                from pypdf import PdfReader
                import io
                reader = PdfReader(io.BytesIO(uploaded_file_ui.read()))
                st.session_state.doc_text = "\n".join(
                    page.extract_text() for page in reader.pages if page.extract_text()
                )
            else:
                raw = uploaded_file_ui.read()
                try:
                    st.session_state.doc_text = raw.decode("utf-8")
                except UnicodeDecodeError:
                    st.session_state.doc_text = raw.decode("latin-1")

    if "doc_text" in st.session_state:
        st.success("Document uploaded successfully!")
    else:
        st.info("Upload a document to get started.")

if "messages" not in st.session_state:
    st.session_state.messages = []  # list of dicts with role and content

# render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question about the uploaded document:")
if prompt:
    if "doc_text" not in st.session_state:
        st.error("Please upload a document first!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user", avatar="👩‍💻"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a document expert assistant. "
                                "Answer questions ONLY using the document below. "
                                "If the answer isn't there, say you don't know.\n\n"
                                f"DOCUMENT:\n{st.session_state.doc_text[:12000]}"
                            )
                        }
                    ] + st.session_state.messages,
                    max_tokens=500,
                    temperature=0.3,
                )
                reply = response.choices[0].message.content
            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})