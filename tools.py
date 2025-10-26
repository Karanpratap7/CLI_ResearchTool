from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool 
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"---Research Output---\nSaved on Timestamp: {timestamp} ---\n\n{data}\n\n"

    with open(filename, "a" , encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}."
@tool(
    "save_to_txt",
    description="Saves the provided research data to a text file named research_output.txt.",
)
def save_to_txt_tool(data: str) -> str:
    return save_to_txt(data)


@tool(
    "web_search",
    description="Useful for when you need to search the web for current information or news about a topic.",
)
def web_search(query: str) -> str:
    search = DuckDuckGoSearchRun()
    return search.run(query)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)