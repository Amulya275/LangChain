from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain

import os
import streamlit as st
from dotenv import load_dotenv

os.environ["huggingfacehub_api_token"]=os.getenv("HUGGINGFACE_API_TOKEN")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_kEY")

# prompt template
prompt_template= ChatPromptTemplate([("system","You a Q&A chatbot. Please respond to queries"),
                                     ("human","question:{input}")])

# Streamlit framework
st.title("LangChain practice with Open Source LLM")
input_text=st.text_input("Search for a topic you want on Data Engineering")

llm= HuggingFaceHub(repo_id="google/gemma-2-2b-it", model_kwargs={"temperature":0.6,"max_length":64})
Output_Parser=StrOutputParser()
llchain=prompt_template|llm|Output_Parser


if input_text:
    st.write(llchain.invoke({"input":input_text}))




