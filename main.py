import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

def read(file):
    readFile = open(file,encoding='utf-8')
    for line in readFile:
        st.text(line) 

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    #Pages#####################################################
    pageIcon = Image.open('./logo/FullLogo.png')
    st.set_page_config(
        page_title='Kristofer Automation',
        page_icon = pageIcon
    )
    #Config####################################################
    hide_st_style = """
        <style>
        #Mainmenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    #Display logo on top#######################################
    logo = Image.open('./logo/FullLogo.png') 
    st.image(logo)
    #Menu######################################################
    selected = option_menu(
        menu_title = 'Meny',
        options = ['Vad jag kan hjälpa till med','CV','Kontakt','Mina kontaktuppgifter'],
        icons = ['','book','envelope'],
        menu_icon = 'cast',
        default_index = 0,
        orientation = 'horizontal',
    )
    if selected == 'Vad jag kan hjälpa till med':
        read('./Files/home.txt')
        # selectExample = st.radio(
        #     'Exempel/förslag',
        #     ["UI"],
        #     captions=[
        #         "OpenSource UI för kommunikation med PLC/IPC (Python pyads/snap7)."],
        #         index=None)

    if selected == 'CV':
        read('./Files/KristoferWestergrenCV.txt')
    if selected == 'Kontakt':
        st.header(':mailbox: Kontakta mig')
        contact_form = """
        <form action="https://formsubmit.co/kristoferautomation@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder=Namn>
            <input type="email" name="email" placeholder=Email>
            <textarea name="message" placeholder="Meddelande"></textarea>
            <button type="submit">Send</button>
        </form
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        local_css("./style/style.css")
    if selected == 'Mina kontaktuppgifter':
        read('./Files/contactInfo.txt') 
    ###########################################################

if __name__ == '__main__':
    main()