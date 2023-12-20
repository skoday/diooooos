from bardapi import BardCookies, Bard  # Importa también Bard para usar ask_about_image
import streamlit as st
from streamlit_chat import message
import io

cookie_dict = {

}

bard = BardCookies(cookie_dict=cookie_dict)

bard = BardCookies(cookie_dict=cookie_dict)

st.title("CalculoIA tutor")

def response_api(promot, image=None):
    if image:
        bard_answer = bard.ask_about_image(promot, image)
    else:
        bard_answer = bard.get_answer(str(promot))
    return bard_answer['content']

def user_input():
    input_text = st.text_input("Introduce lo que necesitas saber: ")
    return input_text

def file_uploader(label):
    uploaded_file = st.file_uploader(label, type=['png', 'jpg', 'jpeg'])
    return uploaded_file

if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input()
user_image = file_uploader("Carga una imagen (opcional):")

if user_text:
    if user_image is not None:
        output = response_api(user_text, image=user_image.read())
    else:
        output = response_api(user_text)
    
    st.session_state['generate'].append(output)
    st.session_state['past'].append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generate"][i], key=str(i))
