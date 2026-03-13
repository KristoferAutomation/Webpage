import streamlit as st
import MyGlobals
from streamlit_option_menu import option_menu

# --- Streamlit config ---
#layout="wide",
st.set_page_config(page_title='Kristofer Automation AB', page_icon=MyGlobals.ICO)
st.html("""<style>Mainmenu {visibility: hidden;}footer {visibility: hidden;}header {visibility: hidden;}""")


st.image(MyGlobals.BANNER)


selected = option_menu(
"Menu",
["Home", "CV", "Contact", "This code"],
icons=["house", "body-text", "envelope-at","code"],
menu_icon="cast",
orientation="horizontal",
default_index=0
)


if selected == "CV":
    st.image(MyGlobals.CV)
elif selected == "Contact":
    st.image(MyGlobals.CARD)
    st.success('note new email: Kristofer@KristoferAutomation.se')
elif selected == "This code":
    st.image(MyGlobals.CODE)
else:
    st.image(MyGlobals.LOGO)

