import streamlit as st
from streamlit_option_menu import option_menu
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from io import BytesIO
from zipfile import ZipFile


# --- Streamlit config ---
st.set_page_config(page_title='PDF Handeler, Kristofer Automation AB', page_icon='./assets/logo.ico')
st.html("""<style>Mainmenu {visibility: hidden;}footer {visibility: hidden;}header {visibility: hidden;}""")


st.image('./assets/banner.png')


# --- Header --
st.header('PDF Handeler',text_alignment='center')


# --- Menu ---
selected = option_menu(
    menu_title='',
    options=['Start','Merge','Split', 'Return'],
    icons=['house','union','subtract','arrow-return-left'],
    menu_icon='cast',
    orientation='horizontal',
    default_index=0
)


# --- Show logo ---
if selected == 'Start':
    st.image('./assets/logo.png')
# --- Merge ---
elif selected == 'Merge':
    upploaded_files = st.file_uploader(label='Uppload pdf documents to merge',
            accept_multiple_files=True,
            type='pdf')
    if len(upploaded_files) >= 2:
        if st.button("Merge PDF's"):
            if upploaded_files:
                merger = PdfMerger()
                for pdf_file in upploaded_files:
                    merger.append(pdf_file)
                merge_pdf = BytesIO()
                merger.write(merge_pdf)
                merger.close()
                merge_pdf.seek(0)
                st.pdf(merge_pdf)
                st.success(f'Merge compleated 🎉')
                st.download_button(
                    label='Download merged PDF',
                    data=merge_pdf,
                    file_name='merged_pdf.pdf',
                    mime='application/pdf'
                )
# --- Split ---
elif selected == 'Split':
    upploaded_file = st.file_uploader(label='Uppload a pdf document to split',
            accept_multiple_files=False,
            type='pdf')
    if upploaded_file:       
        file_bytes = upploaded_file.read()
        pdf_reader = PdfReader(BytesIO(file_bytes)) 
        total_pages = len(pdf_reader.pages)
        st.text(f'Total pages: {total_pages}')
        if total_pages < 2:
            st.error(f'Can not split one page ❌')
        st.pdf(upploaded_file)
        if total_pages > 1:
            split_pos = st.number_input('Select where to split 🔢',step=1,min_value=0)
            if split_pos != 0:
                if split_pos > total_pages -1:
                    st.error(f'Selected larger number then document pages ❌')
                else:                  
                    if st.button("Split"):
                        splits = []
                        #First split part
                        pdf_writer = PdfWriter()
                        for page_num in range(0,split_pos):
                            pdf_writer.add_page(pdf_reader.pages[page_num])
                        pdf_stream = BytesIO()
                        pdf_writer.write(pdf_stream)
                        pdf_stream.seek(0)
                        splits.append(pdf_stream.read())
                        # #Second split part
                        pdf_writer = PdfWriter()
                        for page_num in range(split_pos,total_pages):
                            pdf_writer.add_page(pdf_reader.pages[page_num])
                        pdf_stream = BytesIO()
                        pdf_writer.write(pdf_stream)
                        pdf_stream.seek(0)
                        splits.append(pdf_stream.read())
                        #Generate preview
                        for idx, split_bytes in enumerate(splits, start=1):                           
                            with st.expander(f'Split part {idx} preview'):
                                st.pdf(BytesIO(split_bytes))
                        #Create zip file to download the spiltted files
                        zip_buffer = BytesIO()
                        with ZipFile(zip_buffer,'w') as zip_file:
                            for idx, split_bytes in enumerate(splits, start=1):
                                zip_file.writestr(f'{upploaded_file.name}_split_part_{idx}.pdf',split_bytes)
                        zip_buffer.seek(0)
                        st.success(f'Split compleated 🎉')
                        #Download zipfile
                        st.download_button(
                            'Download splitted files as zip',
                            data=zip_buffer,
                            file_name=f'{upploaded_file.name}_splits.zip',
                            mime='application/zip'
                        )
elif selected == 'Return':
    st.switch_page('app.py')
