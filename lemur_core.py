import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

# Environment Variables
API_KEY = os.getenv("GROQ_API_KEY")


# Initialize Model
def init_model():
    return ChatGroq(model="llama3-8b-8192")


# Conversation History
conversation_history = [
    ("system", "Eres un asistente virtual de la Asociación Científica Especializada en Computación, llamada Acecom. "
               "Tu nombre es Lemuria. Vas a recibir a la entrada de miembros de Acecom al local con un mensaje de "
               "bienvenida agradable.")
    # ("human", "Hi, my name is X"),
    # ("ai", "Nice to meet you X, how can I help you?")
]


# Handle Query
def handle_query(query):
    prompt = ChatPromptTemplate.from_messages(conversation_history[-4:])
    llm = init_model()
    groq_chain = prompt | llm
    response = groq_chain.invoke({"text": query})
    conversation_history.append(("human", query))
    conversation_history.append(("ai", response.content))
    return response.content
