import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

# Create a research agent
def create_research_agent(topic):
    return {
        "messages": [
            {"role": "system", "content": "You are a research specialist."},
            {"role": "user", "content": f"Research the following topic and provide a comprehensive summary: {topic}"}
        ],
        "model": "llama-3.3-70b-versatile",
        "max_completion_tokens": 1000
    }

# Create a writing agent
def create_writing_agent(summary, topic):
    return {
        "messages": [
            {"role": "system", "content": "You are a creative writing specialist."},
            {"role": "user", "content": f"Using the research summary below, write a detailed article on the topic '{topic}':\n\n{summary}"}
        ],
        "model": "llama-3.3-70b-versatile",
        "max_completion_tokens": 1500
    }

# Run the research agent
def run_research_agent(topic):
    research_task = create_research_agent(topic)
    response = client.chat.completions.create(**research_task)
    summary = response.choices[0].message.content
    return summary

# Run the writing agent
def run_writing_agent(summary, topic):
    writing_task = create_writing_agent(summary, topic)
    response = client.chat.completions.create(**writing_task)
    article = response.choices[0].message.content
    return article

# Main program to coordinate multi-agent workflow
if __name__ == "__main__":
    print("Welcome to the Multi-Agent System powered by Groq!")
    topic = input("Enter the research topic: ")
    
    print("\nResearching the topic...")
    research_summary = run_research_agent(topic)
    print("Research Summary:")
    print(research_summary)
    
    print("\nWriting an article based on the research...")
    article = run_writing_agent(research_summary, topic)
    print("Generated Article:")
    print(article)