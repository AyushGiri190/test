
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from context_retriver import retrieve_context
import os 
from dotenv import load_dotenv # Import the function
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.environ.get('gemini_key') # or set it via environment

def get_chatbot_response(user_query: str, chat_history: list) -> str:
    history_str = ""
    for item in chat_history:
        history_str += f"User: {item['query']}\nAssistant: {item['response']}\n"
    context_chunks = retrieve_context(user_query)
    context = "\n\n".join(doc.page_content for doc in context_chunks) if context_chunks else "No relevant context found."

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.1)

    instructions = """Instructions:
    1. Answer only from the context.
    2. If context is not enough, say so.
    3. Be concise and factual.
    4. Use markdown formatting with short headings/tables if needed.
    5. Do not fabricate any information or links.
    6. Have a conversation like normal human being.
    7. Do not specify the amount of information you have for example do not specify that you have information only about tuberculosis, breast cancer,etc."""
    

    full_prompt = f"""
You are a helpful medical assistant. You must answer based on the given context.


User: {user_query}

Context:
{context}

{instructions}

Medical Assistant Response:"""

    prompt = ChatPromptTemplate.from_template(full_prompt)
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"context": context, "user_question": user_query})

    chat_history.append({"query": user_query, "response": result})
    return result
