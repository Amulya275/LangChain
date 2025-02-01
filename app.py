from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from  dotenv import load_dotenv

os.environ["OPEN_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_kEY")

# prompt template
prompt_template= ChatPromptTemplate([("system","You are data engineer.Please respond to queries"),
                                     ("human","{input}")])

# Streamlit framework
st.title("LangChain practice with Open Source LLM")
input_text=st.text_input("Search for a topic you want on Data Engineering")

# LLM initialization

llm=ChatOpenAI(model="gtpt",temperature=0.6)
Output_Parser=StrOutputParser()
chain=prompt_template|llm|Output_Parser

if input_text:
    st.write(chain.invoke({"input":input_text}))