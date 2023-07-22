import streamlit as st
from bardapi import Bard
import requests
import os
import re
import extraction
import database as db


os.environ['_BARD_API_KEY']="XQjG2qxtCj5EwmxI3os2HQEtUckCaigdU8ehzkg_Nx6Kk8NtSCa6-XDFZ4JglugI6qcCnQ."

session = requests.Session()

session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
# We used BARD
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 

bard = Bard(session=session, timeout=30)

def bardCall(prompt,type) :
    
    all_responses=""

    st.write('LLM RUNNING ...')

    questions_set,not_exists,collectionNameRaw,all_questions = extraction.extract()
    print(len(all_questions))
    if(not_exists):
        syllabus = extraction.extract_syllabus()


        for i in range(0,len(questions_set)):
            questions = questions_set[i]

            response=""

            if(type == "condense"):
            #    bard.get_answer('''
                
            #     Start answering after I give you the questions and syllabus. Are you ready? (reply yes or no)''')['content']
                # bard.get_answer(''' I am going to give you a set of questions and a syllabus. I want to you to categorize each question based on what topic in the syllabus it is most related to. (If a question is realted to more than one topic included it in all of them) and rank the topics based on the numbers of questions under each topic and display the top 10 rankings only nothing else.
                #                     Your response should be in the format, nothing extra:
                #                     Example response:
                #                     'topic 1': 'number of questions'
                #                     'topic 2': 'number of questions'. 
                #                     Start answering after I give you the questions and syllabus. Are you ready?''')        
                response=bard.get_answer(f'''I am going to give you a set of questions and a syllabus. I want to you to categorize each question based on what topic in the syllabus it is most related to. (If a question is realted to more than one topic included it in all of them) and rank the topics based on the numbers of questions under each topic and display the top 10 rankings only nothing else.
                                            questions: 
                                            {questions} 
                                            Syllabus: 
                                            {syllabus}''')['content']         
                        
            

            
            # collection.insert_one({'question': response})
            all_responses +=" "+response
            # st.write("RESPONSE : ", response)
            # print(response)
            
    pattern = r"([a-zA-Z]+)\.pdf$"
    match = re.search(pattern, collectionNameRaw)
    if(type == "condense"):
        if match:
            collectionName=match.group(1)
            db.db_questions(all_responses,collectionName)
            # db.TopTenTopics()
            st.write("Top 10 topics are: \n",db.TopTenTopics(collectionName))
        
    elif(type == "question"):
        group_size = 35
        num_groups = -(-len(questions_set) // group_size)  # Round up division to handle remaining sentences

        for i in range(num_groups):
            questions = all_questions[i * group_size : (i + 1) * group_size]

            response=""

            bard.get_answer(f'''
            Below I am giving you set of questions and syllabus as a series of prompts, do not generate anything, just understand, reply with "yes" after analysis.
            questions:
            {questions}
            Syllabus:
            {syllabus}''')
        response = bard.get_answer(f''' Enclosed in quotes is a prompt for you to generate questions. Before that
                        keep these things in mind while generating:
                        Generated questions must be according to the style of the questions provided previously
                        [it could be previously given questions. Consider these things while generating any type of question:
                        It could be application level or understanding level. If not asked specifically generate any or both. 
                        It's not necessarily 'wh' questions, it could be like evaluate, determine, explain 
                        something along those terms. It could also be to ask to draw diagrams] and do not generate the answers
                        '{prompt}' ''')['content']
        st.write(response)