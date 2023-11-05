import streamlit as st
#from llama_index import SimpleDirectoryReader
#from llama_index import ServiceContext
#from llama_index.llms import OpenAI
#from llama_index import VectorStoreIndex
#from dotenv import load_dotenv
#import os
#import OpenAI
#load_dotenv()
#openai.api_key=os.getenv("OPENAI_API_KEY")

#with st.sidebar:
#    st.title ("chat with you data")
#    st.markdown('''
#    ## About
#    This is PSE ChatBot
#    - [Google] (www.google.com)
#    - [WB] (www.google.com)
#    - [SearchAds] (www.google.com) 
#                ''')

def main():
    st.header("Chat with your data")
    #reader=SimpleDirectoryReader(input_dir='./Documentation',recursive=True)
    #docs=reader.load_data()
    #service_context=ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", tempreature=0.5,system_prompt="Hello PSE"))
    #Index=VectorStoreIndex.from_documents(docs, service_context=service_context)
    #if query:
     #   chat_engine=index.as_chat_engine(chat_mode="condense_question", verbose=True)
      #  response=chat_engine.chat(query)
       # st.write(response.response)

if __name__ =='__main__':
    main()

    
