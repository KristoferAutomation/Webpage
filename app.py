import streamlit as st
import streamlit_option_menu


# --- Streamlit config ---
st.set_page_config(page_title='Kristofer Automation AB', page_icon='./assets/logo.ico')
st.html("""<style>Mainmenu {visibility: hidden;}footer {visibility: hidden;}header {visibility: hidden;}""")


st.image('./assets/banner.png')


# --- Header --
st.header('Main page',text_alignment='center')


selected = streamlit_option_menu.option_menu(
    menu_title='',
    options=["Home", "CV", "Contact", "PDF-Handeler"],
    icons=["house", "body-text", "envelope-at", "filetype-pdf"],
    menu_icon="cast",
    orientation="horizontal",
    default_index=0
)


if selected == "CV":
    st.image('./assets/CV.png')
elif selected == "Contact":
    st.image('./assets/card.png')
    st.success('note new email: Kristofer@KristoferAutomation.se')
elif selected == "PDF-Handeler":
    st.switch_page('./pages/pdf_handeler.py')
else:
    st.image('./assets/logo.png')

