from google.generativeai.types.discuss_types import ResponseDict
import streamlit as st
import os
import google.generativeai as genai
# from streamlit.delta_generator import Value
genai.configure(api_key=os.environ['GOOGLE_AI_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-pro')

## function to load Gemini Pro model and get response

def get_gemini_response(question):
	response = model.generate_content(question)
	return response.text


# <--- start of streamlit app code --->

st.set_page_config(page_title="Text Search with Gemini")

st.header("Text Search with Gemini")

st.text("Enter your prompt below :")
user_input = st.text_input("e.g :- What is life ? / जिंदगी क्या है ?", key="user_input")

submit = st.button("Ask to Gemini")

# When submit is clicked :
if user_input or submit:
	response = get_gemini_response(user_input)
	st.write(response)

# <--- end of streamlit app code --->