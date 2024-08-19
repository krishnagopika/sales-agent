from langchain.agents import  AgentExecutor, load_tools, create_openai_tools_agent, create_react_agent
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_openai.chat_models import AzureChatOpenAI

from tools.job_search_tool import job_search_tool
from prompts.agent_prompt import agent_prompt
from dotenv import load_dotenv

load_dotenv()

import os

api_key = os.getenv('AZURE_OPENAI_API_KEY')
api_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
openai_api_version=os.getenv("OPENAI_API_VERSION")
openai_api_type=os.getenv("OPENAI_API_TYPE")
azure_deployment=os.getenv("AZURE_DEPLOYMENT")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            agent_prompt,
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

llm = AzureChatOpenAI(temperature=0.4, model_name="gpt-4o", azure_deployment=azure_deployment, azure_endpoint=api_endpoint, api_key=api_key, openai_api_version=openai_api_version, openai_api_type=openai_api_type)

tools = load_tools([], llm=llm)
tools.append(job_search_tool)

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)