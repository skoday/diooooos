from bardapi import BardCookies
import streamlit as st
from streamlit_chat import message
import subprocess

cookie_dict = {
}

bard = BardCookies(cookie_dict=cookie_dict)


st.title("Testing????????????????????????????")

def response_api(promot, image=None):
    if image:
        bard_answer = bard.ask_about_image(promot, image)
    else:
        bard_answer = bard.get_answer(str(promot))
    return bard_answer['content']

def user_input():
    input_text = st.text_input("Prompt: ")
    return input_text

def file_uploader(label):
    uploaded_file = st.file_uploader(label, type=['png', 'jpg', 'jpeg'])
    return uploaded_file

def reconocer_voz():
    texto = None
    try:
        texto = subprocess.check_output(['python', 'speech.py']).decode().strip()
    except subprocess.CalledProcessError as e:
        print("Error al intentar obtener la transcripción de audio:", e)
    return texto

if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input()
user_image = file_uploader("Upload an image (optional):")

if st.button("Talk"):
    audio_text = reconocer_voz()
    if audio_text:
        if user_image is not None:
            output = response_api(audio_text, image=user_image.read())
        else:
            output = response_api(audio_text)
        
        st.session_state['generate'].append(output)
        st.session_state['past'].append("Audio: " + audio_text)

if st.button("Send"):
    if user_text:
        if user_image is not None:
            output = response_api(user_text, image=user_image.read())
        else:
            output = response_api(user_text)
    
        st.session_state['generate'].append(output)
        st.session_state['past'].append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        if i % 2 == 0:
            st.markdown(
                f"""<div style="background-color: #277DA1; padding: 10px; border-radius: 15px; margin: 10px 50px; color: #ffffff;">
                    <p style="font-weight: bold;">{st.session_state["past"][i]}</p>
                    <p>{st.session_state["generate"][i]}</p>
                </div>""",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""<div style="background-color: #277DA1; padding: 10px; border-radius: 15px; margin: 10px 50px; color: #ffffff;">
                    <p style="font-weight: bold;">{st.session_state["past"][i]}</p>
                    <p>{st.session_state["generate"][i]}</p>
                </div>""",
                unsafe_allow_html=True
            )
