import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Environment Variables
API_KEY = os.getenv("GROQ_API_KEY")


# Initialize Model
def init_model():
    return ChatGroq(model="llama3-8b-8192")


# Conversation History
conversation_history = [
    ("system", "You are a helpful assistant called LemurAI."),
    ("human", "Hi, my name is Jared"),
    ("ai", "Nice to meet you Jared, how can I help you?")
]


# Handle Query
def handle_query(question):
    prompt = ChatPromptTemplate.from_messages(conversation_history[-2:])
    llm = init_model()
    groq_chain = prompt | llm
    response = groq_chain.invoke({"text": question})
    conversation_history.append(("human", question))
    conversation_history.append(("ai", response.content))
    return response.content
