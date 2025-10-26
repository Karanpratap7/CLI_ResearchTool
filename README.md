# Research Tool

This project is a Python-based research assistant that uses AI to answer user queries. It generates a research report including a summary, sources, and a list of tools used.

## How it Works

1.  The user enters a research query.
2.  The AI agent, built with `langchain`, uses a combination of web search (`DuckDuckGoSearchRun`) and Wikipedia search (`WikipediaQueryRun`) to gather information.
3.  The agent then generates a research report with a summary and a list of sources.
4.  The report is automatically saved to a file named `research_output.txt`.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/research-tool.git
    cd research-tool
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** and add your Google API key:
    ```
    GOOGLE_API_KEY="your-api-key"
    ```

5.  **Run the application:**
    ```bash
    python main.py
    ```

## Files

*   `main.py`: The main entry point of the application. It takes user input, runs the research agent, and prints the output.
*   `tools.py`: Defines the tools used by the agent, including web search, Wikipedia search, and a tool to save the output to a file.
*   `requirements.txt`: A list of the Python packages required to run the project.
*   `research_output.txt`: The file where the research reports are saved.
*   `.gitignore`: Specifies which files and directories to ignore in the Git repository.
