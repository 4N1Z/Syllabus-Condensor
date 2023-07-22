from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import os
import os
from bard import bardCall
import time
# import 
from dotenv import load_dotenv,dotenv_values


load_dotenv()
os.environ['_BARD_API_KEY']=os.getenv('_BARD_API_KEY')

# Fucntion to save the PDF to directory
def save_uploadedfile(uploadedfile, path):
     with open(os.path.join("data",path,uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to directory".format(uploadedfile.name))


def get_names(pdf):
     #adding the names of upload to a list
    check_pdf = []
    for uploaded_file in pdf:
        check_pdf.append(uploaded_file.name)


def main():
    # load_dotenv()

    st.set_page_config(page_title='Syllabus GPT',)
    st.header("Give your prompt based on the Uploaded Docs")

    #getting the upload 
    with st.sidebar:
        st.header("Upload the PDF's")
        pdf_s = st.file_uploader("Upload the sylabbus",accept_multiple_files=True,type=['pdf', 'docx','txt'])
        pdf_q = st.file_uploader("Upload the Question paper: Rename question paper to 'year_semester_subject' eg: 2019_1_physics",accept_multiple_files=True,type=['pdf', 'docx'])

        pdf_s_names = get_names(pdf_s)
        pdf_q_names = get_names(pdf_q)
        st.write(pdf_q_names,pdf_s_names)


        if st.button("Analyze"):
            if pdf_s and pdf_q is not None: 
                for eachFile in pdf_s:
                    save_uploadedfile(eachFile,"syllabus")
                for eachFile in pdf_q:
                    save_uploadedfile(eachFile,"questionPaper")
            if pdf_s is not None:
                for eachFile in pdf_s:
                    save_uploadedfile(eachFile,"syllabus")
            elif pdf_q is not None:
                for eachFile in pdf_q:
                    save_uploadedfile(eachFile,"questionPaper")
             
            if len(pdf_s) == 0 or len(pdf_q) == 0:
                st.write("PDF's not Found") 
            else:
                bardCall("","condense")
               
    take_prompt = st.text_input("Enter the prompt")

    if st.button("Generate"):
        if len(take_prompt) is 0:
            st.write("Prompt not found")
        else :
            bardCall(take_prompt,"question")

    
    # generate_env_example()
    # st.write(bardCall())

def delete_files():
    file_list = os.listdir("./data/syllabus")
    for file_name in file_list:
        file_path = os.path.join("./data/syllabus", file_name)
        os.remove(file_path)
    file_list = os.listdir("./data/questionPaper")
    for file_name in file_list:
        file_path = os.path.join("./data/questionPaper", file_name)
        os.remove(file_path)

if __name__ == '__main__':

    main()
    # time.sleep(45)
    # delete_files()
    