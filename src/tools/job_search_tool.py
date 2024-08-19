import os
from langchain_community.tools.google_jobs import GoogleJobsQueryRun
from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper
from langchain.tools.base import StructuredTool
from dotenv import load_dotenv
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain_core.tools import Tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool



load_dotenv()

#serper_api_key= os.getenv["SERPAPI_API_KEY"]
job_search = GoogleJobsQueryRun(api_wrapper=GoogleJobsAPIWrapper())

# class CustomSearchTool(BaseTool):
#     name = "job_search"
#     description = "useful for when you need jobs info about a specific company"
#     # args_schema: Type[BaseModel] = SearchInput

#     def _run(
#         self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
#     ) -> str:
#         """Use the tool."""
#         return job_search.run(query)

def job_search_function(query: str):
    return job_search.run(query)

job_search_tool = StructuredTool.from_function(
    name="google_job",
    description="Performs a Google search for jobs.",
    func=job_search_function,
)


# to test the job search tool with summarization
# result = job_search_tool.run("Can I get an entry level software eng job posting in jpmc")

# print(result)