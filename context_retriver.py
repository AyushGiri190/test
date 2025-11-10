from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from config import PINECONE_INDEX_NAME
from dotenv import load_dotenv
import os 
from dotenv import load_dotenv # Import the function
load_dotenv()
os.environ["PINECONE_API_KEY"] =os.environ.get('pinecone_key')
load_dotenv()
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

def retrieve_context(user_query: str, top_k=5):
    index = pc.Index(PINECONE_INDEX_NAME)
    vectorstore = PineconeVectorStore.from_existing_index(
        index_name=PINECONE_INDEX_NAME,
        embedding=embeddings
    )
    return vectorstore.similarity_search(user_query, k=top_k)
