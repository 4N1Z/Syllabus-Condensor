import re
import PyPDF2
import os
import streamlit as st
import database as db

input_dir = "./data/questionPaper"
output_dir= "./output"

def read_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(f)

        # Extract text content from each page
        text_content = ""
        for page_num in range(len(pdf_reader.pages)):   
            page = pdf_reader.pages[page_num]
            text_content += page.extract_text()
    return text_content

def remove_leading_whitespace(text):
    lines = text.split('\n')
    stripped_lines = [line.lstrip() for line in lines]
    return '\n'.join(stripped_lines)

def process_pdf_file(pdf_file_path):
    text = read_pdf(pdf_file_path)
    text = remove_leading_whitespace(text)

    pattern = r'^(?:(\d+)|[a-z]\))\s+(.*?)(?=\s*\(\d+\))'  # Updated regular expression pattern

    questions = re.findall(pattern, text, flags=re.MULTILINE | re.DOTALL)

    output_file_name = os.path.splitext(os.path.basename(pdf_file_path))[0] + ".txt"
    output_file_path = os.path.join(output_dir, output_file_name)

    text=""
    i=1
    for question_number, question_text in questions:
        question_text = re.sub(r'^[a-z]\)\s*', '', question_text)
        text += f"Question {i} {question_text}\n"
        i += 1
    return text

# def extract():
#     for file_name in os.listdir(input_dir):
#         if file_name.endswith(".pdf"):
#             pdf_file_path = os.path.join(input_dir, file_name)
#             return process_pdf_file(pdf_file_path)

def extract():
    not_exists=False
    st.write("Extracting Questions")
    questions=[]
    all_questions=[]
    for file_name in os.listdir(input_dir):
        if db.CheckIfFileExistsInDatabase(file_name):
            pdf_file_path = os.path.join(input_dir, file_name)
            all_questions.append(process_pdf_file(pdf_file_path))
            continue
        elif file_name.endswith(".pdf"):                      # Todo: if file not in database then only extract, If file in database then skip
            not_exists=True
            pdf_file_path = os.path.join(input_dir, file_name)
            all_questions.append(process_pdf_file(pdf_file_path))
            questions.append(process_pdf_file(pdf_file_path))
    # st.write("FROM EXTRACTION : " , questions)
    # print(len(all_questions)," yooo \n")
    return questions,not_exists,file_name,all_questions

def extract_syllabus():

    st.write("Extracting syllabus")

    file_path = "./data/syllabus"
    file_contents=""
    for filename in os.listdir(file_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(file_path, filename)

            with open(file_path, 'r') as file:
                file_contents = file.read()

    return file_contents