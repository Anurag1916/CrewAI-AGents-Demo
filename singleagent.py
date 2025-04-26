# import os
# from dotenv import load_dotenv
# from crewai import Agent, Task, Crew
# from crewai_tools import SerperDevTool
# from langchain_openai import ChatOpenAI
# from euriai import EuriaiClient

# load_dotenv()

# SERPER_API_KEY = os.getenv("SERPER_API_KEY")
# EURI_API_KEY = os.getenv("EURI_API_KEY")

# search_tool = SerperDevTool()

# euriai_client = EuriaiClient(api_key=EURI_API_KEY )
# def create_research_agent():

#     # llm = ChatOpenAI(model="gpt-3.5-turbo")
  
#     return Agent(
#         role="Research Specialist",
#         goal="Conduct thorough research on given topics",
#         backstory="You are an experienced researcher with expertise in finding and synthesizing information from various sources",
#         verbose=True,
#         allow_delegation=False,
#         tools=[search_tool],
#         llm=euriai_client,
#     )




# def create_research_task(agent, topic):
#     return Task(
#         description=f"Research the following topic and provide a comprehensive summary: {topic}",
#         agent=agent,
#         expected_output = "A detailed summary of the research findings, including key points and insights related to the topic"
#     )

# def run_research(topic):
#     agent = create_research_agent()
#     task = create_research_task(agent, topic)
#     crew = Crew(agents=[agent], tasks=[task])
#     result = crew.kickoff()
#     return result

# if __name__ == "__main__":
#     print("Welcome to the Research Agent!")
#     topic = input("Enter the research topic: ")
#     result = run_research(topic)
#     print("Research Result:")
#     print(result)



import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Load the Groq API key from the environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

def create_research_task(topic):
    """
    Create a research task using the Groq API.
    """
    return {
        "messages": [
            {"role": "system", "content": "You are a research specialist."},
            {"role": "user", "content": f"Research the following topic and provide a comprehensive summary: {topic}"}
        ],
        "model": "llama-3.3-70b-versatile",  # Specify the Groq model to use
        "max_completion_tokens": 1000  # Adjust token limit as needed
    }

def run_research(topic):
    """
    Run the research task using the Groq API.
    """
    task = create_research_task(topic)
    response = client.chat.completions.create(**task)
    
    # Access the content properly
    result = response.choices[0].message.content
    return result

if __name__ == "__main__":
    print("Welcome to the Research Agent powered by Groq!")
    topic = input("Enter the research topic: ")
    result = run_research(topic)
    print("Research Result:")
    print(result)