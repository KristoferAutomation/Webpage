import streamlit as st
import streamlit_option_menu


# --- Streamlit config ---
st.set_page_config(page_title='Kristofer Automation AB', page_icon='logo.ico')
st.html("""<style>Mainmenu {visibility: hidden;}footer {visibility: hidden;}header {visibility: hidden;}""")


st.image('banner.png')


selected = streamlit_option_menu.option_menu(
"Menu",
["Home", "CV", "Contact"],
icons=["house", "body-text", "envelope-at"],
menu_icon="cast",
orientation="horizontal",
default_index=0
)


if selected == "CV":
    st.image('CV.png')
elif selected == "Contact":
    st.image('card.png')
    st.success('note new email: Kristofer@KristoferAutomation.se')
else:
    st.image('logo.png')

