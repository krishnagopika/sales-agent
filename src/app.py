import streamlit as st
from sales_agent import agent_executor
from tools.web_retriever_tool import qa_chain
from tools.job_search_tool import job_search_tool
# Title of the page
st.title('Revature Bot')
 

# Code to add the first ai message
if 'chat' not in st.session_state:
  st.session_state['chat'] = [{
    "content": "Hi, I'm a revature bot. How can I help you today?",
    "role": "ai"
  }]

user_input = st.chat_input('message:', key= "user_input")

# adding user input to session
if user_input:
  st.session_state['chat'].append({
    "content": user_input,
    "role": "user"
  })

  # calling retreival chain to get content and sources

  result = qa_chain({"question": user_input})
  # result = {"answer": "not much", "sources":"NA"}
  content = result['answer']
  sources = result['sources']
  # calling the langchain sales agent
  agent_response = agent_executor.invoke({"company": user_input, "content": content, "sources": sources})
  # adding ai agent response to the session state
  st.session_state['chat'].append({
    "content": agent_response['output'],
    "role": "ai"})
  # except :
  #   # handlinig any parsing errors
  #   st.session_state['chat'].append({
  #     "content": "Sorry, I'm not sure I can help with that.",
  #     "role":"ai"})

# rendering the messesges from chat
if st.session_state['chat']:
  for i in range(0, len(st.session_state['chat'])):
    user_message = st.session_state['chat'][i]
    st.chat_message(user_message["role"]).write(user_message["content"])
