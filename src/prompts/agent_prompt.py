agent_prompt = """/
Use the google_jobs tool exclusively for job search information related to the specified company. 
Do not use this tool for general company information or other purposes.

For the company specified, provide a comprehensive analysis covering:

Provide a detailed analysis of the {company}'s entry level new hire needs and workforce upskilling requirements, focusing on:
Count of current open positions by technology
current and planned projects and initiatives
key technology applications and use cases
required skills and qualifications for relevant roles
strategic goals and partnerships related to the technology
scale of initiatives and potential areas for external support
Include a brief company overview and recent success stories. Provide links to recent, reputable sources.
From the provided reponses from tools draft the answer as mentioned above and links to source documents at the end.

Use the provided content and sources for context on company information, projects, initiatives, and other non-job-specific details.

content: {content}
sources: {sources}

Incorporate data from the google_jobs tool specifically for job-related information (open positions, skills, qualifications).


Draft a detailed response addressing all these points. Include links to recent, reputable sources at the end of your analysis.

Thought:{agent_scratchpad}
"""