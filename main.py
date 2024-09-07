from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Here is the Conversation History: {context}

Question: {question}

Answer:
"""

def start_conversation():
    context = ""
    print("Welcome to AI chatbot")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        res = chain.invoke({"context" : context, "question" : user_input})
        print("Llama3 :", res)
        context = f"\nUser: {user_input}\nLlama3: {res}"

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

if __name__ == "__main__":
    start_conversation()