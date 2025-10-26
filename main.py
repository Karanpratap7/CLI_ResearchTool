from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import web_search, wiki_tool, save_to_txt_tool


load_dotenv()  

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str] 

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that generates a research report.
            Answer the user query in detail.
            Include:
            - A summary paragraph explaining the answer.
            - Sources (URLs, books, articles, etc.).
            - Tools you used to gather information.

            Wrap the output exactly in this format: {format_instructions}
            Provide no other text.
    """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_agent(
    model=llm,
    tools=[web_search, wiki_tool, save_to_txt_tool],
)

user_query = input("Enter your research query: ")

raw_response = agent.invoke({
    "messages": [
        {"role": "system", "content": prompt.format(query=user_query)},
        {"role": "user", "content": user_query}
    ]
})


#pprint.pprint(raw_response["messages"][3].content, width=200)
print(raw_response["messages"][4].content)

# Automatically save response to file
from tools import save_to_txt_tool
response_text = raw_response["messages"][4].content
save_to_txt_tool.invoke({"data": response_text})

