# This tool takes the history of the chat and generates related/guided questions that users can then ask as a follow up.

from langchain import LLMChain
from langchain import PromptTemplate
from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()



llm = AzureChatOpenAI(deployment_name="demo-models", model_name="gpt-35-turbo")

suggested_user_prompts = """
You are an supportive and honest agent for Revature, a talent enablement company. You help Revature's sales agents. You want to gently guide them to learn more about Revature's offering and to see the sample curricula. 
Based on the chat history, generate three questions for the users to ask next.
Provide exactly three questions in a plain list format, without enumerators or dashes in front.
Chat history: {chat_history}
"""
question_prompt_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(suggested_user_prompts)
)