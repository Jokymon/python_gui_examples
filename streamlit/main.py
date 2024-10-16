import streamlit as st


st.set_page_config(page_title="Streamlit GUI Beispiel")

st.write("Lass dich begrüssen")
st.text_input("Wie ist dein Name?", key="name")
if st.button("Begrüsse"):
    st.write(f"Hallo {st.session_state.name}")
