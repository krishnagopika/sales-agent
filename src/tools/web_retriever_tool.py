from langchain.retrievers.web_research import WebResearchRetriever
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_openai import AzureChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.upstash import UpstashVectorStore
from langchain.callbacks.base import BaseCallbackHandler
from langchain.tools.retriever import create_retriever_tool

from dotenv import load_dotenv

load_dotenv()

import logging

logging.basicConfig()
logging.getLogger("langchain.retrievers.web_research").setLevel(logging.INFO)

import os

api_key = os.getenv('AZURE_OPENAI_API_KEY')
api_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
openai_api_version=os.getenv("OPENAI_API_VERSION")
openai_api_type=os.getenv("OPENAI_API_TYPE")
azure_deployment=os.getenv("AZURE_DEPLOYMENT")

# Vectorstore
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = UpstashVectorStore(embedding=embeddings, index_token = os.getenv('UPSTASH_VECTOR_REST_TOKEN'), index_url = os.getenv('UPSTASH_VECTOR_REST_URL') )
llm = AzureChatOpenAI(temperature=0.4, model_name="gpt-4o", azure_deployment=azure_deployment, azure_endpoint=api_endpoint, api_key=api_key, openai_api_version=openai_api_version, openai_api_type=openai_api_type)

# Search
search = GoogleSearchAPIWrapper()

# Initialize
web_research_retriever = WebResearchRetriever.from_llm(
    vectorstore=vectorstore, llm=llm, search=search, allow_dangerous_requests= True, num_search_results=3
)

# Run

# Retrival Chain imput to the agent
from langchain.chains import RetrievalQAWithSourcesChain

qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm, retriever=web_research_retriever
)

# retreival tool for the agent
# web_retreiver_tool = create_retriever_tool(
#     web_research_retriever,
#     "web_search_tool",
#     "Searches and returns company info and talent enabelement requirements",
# )

# Handeler for retreiver agent

# class StreamHandler(BaseCallbackHandler):
#     def __init__(self, container, initial_text=""):
#         self.container = container
#         self.text = initial_text

#     def on_llm_new_token(self, token: str, **kwargs) -> None:
#         self.text += token
#         self.container.info(self.text)


# class PrintRetrievalHandler(BaseCallbackHandler):
#     def __init__(self, container):
#         self.container = container.expander("Context Retrieval")

#     def on_retriever_start(self, query: str, **kwargs):
#         self.container.write(f"**Question:** {query}")

#     def on_retriever_end(self, documents, **kwargs):
#         # self.container.write(documents)
#         for idx, doc in enumerate(documents):
#             source = doc.metadata["source"]
#             self.container.write(f"**Results from {source}**")
#             self.container.text(doc.page_content)

