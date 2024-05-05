from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# SET UP MODEL
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])


def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

# STREAMLIT APP SETUP
st.set_page_config("Question and Answer Chatbot")

st.header("Gemini LLM")

# create a session state if history is not there 
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

# text input  
input=st.text_input("Input: ",key="input")
submit=st.button("Ask Question to Gemini")

if submit and input:
    response=get_gemini_response(input)
    # add session state
    st.session_state['chat_history'].append(("You :",input))
    st.subheader("Response")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini :",chunk.text))
st.subheader("History")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}{text}")
